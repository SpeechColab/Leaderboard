#!/usr/bin/env python3
# Request and batch_client module must be installed.
# Run pip install requests if necessary.
# doc: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription

import codecs
import json
import requests
import sys
import time

MAX_RETRY = 10
RETRY_INTERVAL = 1.0
REGION = 'chinaeast2'
LOCALE = "zh-CN"
NAME = "Microsoft batch transcription"
DESCRIPTION = "Microsoft batch transcription description"
#HOST = "https://{REGION}.api.cognitive.azure.cn/speechtotext/v3.1" .format(REGION=REGION)
HOST = "https://eastasia.api.cognitive.microsoft.com/speechtotext/v3.1"

with open('SUBSCRIPTION_KEY', 'r') as f:
    SUBSCRIPTION_KEY = f.readline().strip()
    HEADERS = {"Content-Type": "application/json", "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY}


def recognize(audio):
    text = ''
    for i in range(MAX_RETRY):
        try:
            rec = do_recognition(audio)
            if rec != '':
                text = rec
                break
        except Exception as e:
            sys.stderr.write("exception, retrying:{}\n".format(str(e)))
            sys.stderr.flush()
            time.sleep(RETRY_INTERVAL)
    return text


def do_recognition(audio):
    text = ''
    result_list = []

    # create the batch transcription
    (transcription_self_url, transcription_files_url) = create_transcrption(audio)

    # get the transcription Id from the location URI
    transcription_id = transcription_self_url.split("/")[-1]

    print("Created new transcription with id '{transcription_id}' in region {REGION}".format(transcription_id=transcription_id, REGION=REGION))
    print("Checking status.")

    completed = False
    while not completed:
        # wait for 5 seconds before refreshing the transcription status
        time.sleep(5)
        status = get_transcrption_status(transcription_self_url)
        print("Transcriptions status: {status}.".format(status=status))
        if status in ("Failed", "Succeeded"):
            completed = True

        if status == "Succeeded":
            page_files = get_transcrption_files(transcription_files_url)
            for file_data in page_files:
                if file_data["kind"] != "Transcription":
                    continue

                content_url = file_data["links"]["contentUrl"]
                results = requests.get(content_url)
                results_object = json.loads(results.content.decode('utf-8'))
                recognizedPhrases = results_object['recognizedPhrases']
                if len(recognizedPhrases) > 0:
                    for phrase in recognizedPhrases:
                        nBest = phrase['nBest']
                        result_list.append(nBest[0]['lexical'])
                else:
                    print("Transcriptions result is null.")
        elif status == "Failed":
            sys.stderr.write("Transcription failed.")
            sys.stderr.flush()

    text = " ".join(result_list)
    print("Transcriptions text: {text}".format(text=text))

    # Delete transcription
    delete_transcrption(transcription_self_url)
    print("Deleted transcription with id {transcription_id}.\n".format(transcription_id=transcription_id))

    return text


def create_transcrption(audio):
    data = {
        "locale": LOCALE,
        "contentUrls": [audio],
        "displayName": NAME,
        "description": DESCRIPTION,
        "properties": {"profanityFilterMode": "None"}
    }
    url = HOST + "/transcriptions"
    results = requests.post(url, headers=HEADERS, json=data)
    results_object = json.loads(results.content.decode('utf-8'))
    transcription_self_url = results_object["self"]
    transcription_files_url = results_object["links"]["files"]

    return (transcription_self_url, transcription_files_url)


def get_transcrption_status(url):
    results = requests.get(url, headers=HEADERS)
    results_object = json.loads(results.content.decode('utf-8'))
    transcription_status = results_object["status"]

    return transcription_status


def get_transcrption_files(url):
    results = requests.get(url, headers=HEADERS)
    results_object = json.loads(results.content.decode('utf-8'))
    transcription_files = results_object["values"]

    return transcription_files


def delete_transcrption(url):
    results = requests.delete(url, headers=HEADERS)
    return (results.status_code)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("asr_batch.py <in_scp> <out_trans>\n")
        exit(-1)
    scp = codecs.open(sys.argv[1], 'r',  'utf8')
    trans = codecs.open(sys.argv[2], 'w+', 'utf8')

    n = 0
    for l in scp:
        l = l.strip()
        if (len(l.split('\t')) == 2):  # scp format: "key\taudio"
            key, audio = l.split(sep="\t", maxsplit=1)
            print(str(n) + '\tkey:' + key + '\taudio:' + audio)

            text = ''
            text = recognize(audio)

            trans.write(key + '\t' + text + '\n')
            trans.flush()
            n += 1
        else:
            sys.stderr.write("Invalid line: " + l + "\n")
            sys.stderr.flush()

    scp.close()
    trans.close()
