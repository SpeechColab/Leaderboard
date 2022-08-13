#!/usr/bin/env python3
# Request module must be installed.
# Run pip install requests if necessary.
# doc: https://docs.azure.cn/zh-cn/cognitive-services/speech-service/rest-speech-to-text

import codecs
import json
import sys
import time
import azure.cognitiveservices.speech as speechsdk

MAX_RETRY = 10
RETRY_INTERVAL = 1.0
REGION = 'chinaeast2'
LOCALE = "en-US"
with open('SUBSCRIPTION_KEY', 'r') as f:
    SUBSCRIPTION_KEY = f.readline().strip()


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

    try:
        speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION_KEY, region=REGION)
        speech_config.speech_recognition_language = LOCALE
        speech_config.set_profanity(speechsdk.ProfanityOption.Raw)
        speech_config.output_format = speechsdk.OutputFormat.Detailed
        audio_input = speechsdk.AudioConfig(filename=audio)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

        text = ''
        result_list = []
        done = False

        def session_stopped(evt):
            nonlocal done
            done = True

        def canceled(evt):
            nonlocal done
            done = True
            result = evt.result
            if result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    sys.stderr.write("Error details: {}".format(cancellation_details.error_details)+"\n")
                    sys.stderr.flush()

        def recognized(evt):
            result = evt.result
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                nBest = json.loads(result.json)['NBest']
                result_list.append(nBest[0]['Lexical'])

        speech_recognizer.recognized.connect(recognized)
        speech_recognizer.session_stopped.connect(session_stopped)
        speech_recognizer.canceled.connect(canceled)

        # Start continuous speech recognition
        speech_recognizer.start_continuous_recognition()
        while not done:
            time.sleep(1)
        # Stop continuous speech recognition
        speech_recognizer.stop_continuous_recognition()

        text = " ".join(result_list)
    except Exception as e:
        sys.stderr.write("exception, retrying:{}\n".format(str(e)))
        sys.stderr.flush()
        time.sleep(RETRY_INTERVAL)

    return text


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("asr_sdk.py <in_scp> <out_trans>\n")
        sys.stderr.flush()
    scp = codecs.open(sys.argv[1], 'r',  'utf8')
    trans = codecs.open(sys.argv[2], 'w+', 'utf8')

    n = 0
    for l in scp:
        l = l.strip()
        if (len(l.split('\t')) == 2):  # scp format: "key\taudio"
            key, audio = l.split(sep="\t", maxsplit=1)
            sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
            sys.stderr.flush()

            text = ''
            text = recognize(audio)
            
            # delete the space before 's
            # e.g.  in Apron 's early years  ->  in Apron's early years     
            text = text.replace(' \'s','\'s')
            
            sys.stderr.write(text+"\n")
            sys.stderr.flush()
            trans.write(key + '\t' + text + '\n')
            trans.flush()
            n += 1
        else:
            sys.stderr.write("Invalid line: " + l + "\n")
            sys.stderr.flush()

    scp.close()
    trans.close()
