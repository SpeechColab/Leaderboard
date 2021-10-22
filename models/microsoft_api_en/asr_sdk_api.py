#!/usr/bin/env python3
# Request module must be installed.
# Run pip install requests if necessary.
# doc: https://docs.azure.cn/zh-cn/cognitive-services/speech-service/rest-speech-to-text

import sys
import time
import codecs
import azure.cognitiveservices.speech as speechsdk

MAX_RETRY=10
RETRY_INTERVAL=1.0
Region='westus'
Locale="en-US"
SUBSCRIPTION_KEY=''
with open('', 'r') as f:
    SUBSCRIPTION_KEY = f.readline().strip()

def recognize(audio):

    speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION_KEY, region=Region)
    speech_config.speech_recognition_language = Locale
    audio_input = speechsdk.AudioConfig(filename=audio)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    text = ''
    for i in range(MAX_RETRY):
        try:
            result = speech_recognizer.recognize_once_async().get()
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                text = result.text
                sys.stdout.write("Recognized: {}".format(result.text))
                break
            elif result.reason == speechsdk.ResultReason.NoMatch:
                sys.stderr.write("No speech could be recognized: {}".format(result.no_match_details))
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                sys.stderr.write("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    sys.stderr.write("Error details: {}".format(cancellation_details.error_details))
            sys.stderr.flush()
            time.sleep(RETRY_INTERVAL)
        except:
            sys.stderr.write("exception, retrying\n")
            time.sleep(RETRY_INTERVAL)
    return text

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("asr_api.py <in_scp> <out_trans>\n")
    scp   = codecs.open(sys.argv[1], 'r',  'utf8')
    trans = codecs.open(sys.argv[2], 'w+', 'utf8')
 
    n = 0
    for l in scp:
        l = l.strip()
        if (len(l.split('\t')) == 2): # scp format: "key\taudio"
            key, audio = l.split(sep="\t", maxsplit=1)
            sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
            sys.stderr.flush()

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