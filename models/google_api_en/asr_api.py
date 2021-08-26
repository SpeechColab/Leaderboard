#!/usr/bin/env python3
# coding: utf8
'''
Cloud Speech-to-Text API documentation entry can be found here:
    https://cloud.google.com/speech-to-text/
    https://cloud.google.com/speech-to-text/docs/sync-recognize#speech-sync-recognize-python
'''

# [START speech_transcribe_sync]
from google.cloud import speech

import io, sys
import codecs

def transcribe_file(client, file_name):
    """
    Transcribe a short audio file using synchronous speech recognition
    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """
    # Instantiates a client
    #client = speech_v1.SpeechClient()

    # The language of the supplied audio
    #language_code = "en-US"
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    model_type="video"

    with io.open(file_name, 'rb') as f:
        content = f.read()
    
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        language_code = language_code,
        sample_rate_hertz = sample_rate_hertz,
        encoding = encoding,
        model = model_type)

    response = client.recognize(config=config, audio=audio)

    #for result in response.results:
    #    # First alternative is the most probable result
    #    alternative = result.alternatives[0]
    #    print(u"Transcript: {}".format(alternative.transcript))

    rec_text = ''
    for result in response.results:
        rec_text += result.alternatives[0].transcript
    return rec_text
# [END speech_transcribe_sync]

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("rest_api.py <in_scp> <out_trans>\n")
        exit(-1)

    SCP = sys.argv[1]
    TRANS = sys.argv[2]

    client = speech.SpeechClient()

    scp_file = open(SCP, 'r', encoding='utf8')
    trans_file = open(TRANS, 'w+', encoding='utf8')

    n = 0
    for l in scp_file:
        l = l.strip()
        if l == '':
            continue

        key, audio = l.split('\t')
        sys.stderr.write(str(n) + '\tkey:' + key + '\taudio:' + audio + '\n')
        sys.stderr.flush()

        rec_text = transcribe_file(client, audio)

        trans_file.write(key + '\t' + rec_text + '\n')
        trans_file.flush()
        n += 1

    scp_file.close()
    trans_file.close()

