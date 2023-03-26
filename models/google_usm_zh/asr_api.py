#!/usr/bin/env python3
# coding: utf8

import io, sys
from google.api_core import exceptions
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

class SpeechParameters(object):
  """Holds required parameters to create Speech-to-Text Recognizer.
    A Recognizer is a GCP resource that contains:
      * An identificator, provided by you.
      * A model to use in recognition requests.
      * A language code or locale.
    You can learn more about Recognizers here:
    https://cloud.google.com/speech-to-text/v2/docs/basics#recognizers
  """
  def __init__(self):
    # Recognizer Id. This allowes you to name the Recognizer.
    # Must be unique by GCP project/location.
    self.recognizer_id = 'usmenus' #@param
    # Language code to use with this recognizer.
    #self.locale = 'en-US' # @param
    self.locale = 'zh-Hans-CN' # @param
    # Use the USM model. Don't change if you want to actually use the USM model.
    self.model = 'usm'
    # GCP project to interact with Cloud Speech-to-Text API.
    self.gcp_project = '' #@param

  def base_recognizer_path(self):
      return f'projects/{self.gcp_project}/locations/us-central1'

  def full_recognizer_path(self):
      return f'{self.base_recognizer_path()}/recognizers/{self.recognizer_id}'

#@title Cloud Speech-to-Text Implementation.
class SpeechInterface(object):
  """Implementation of the Cloud Speech-to-Text API.

    Exposes CreateRecognizer and Recognize calls.
  """
  def __init__(self, speech_params: SpeechParameters):
    self.speech_params_ = speech_params
    self.speech_client_ = SpeechClient(
        client_options={
            'api_endpoint': 'us-central1-speech.googleapis.com',
        })
    self.recognizer_ = None


  def CreateRecognizer(self):
    """Creates a Recognizer if it doesn't exist.

      Args: None
      Returns: None
    """
    need_to_create_recognizer = False
    # Fetch recognizer, or create it if it doesn't exist.

    try:
        self.recognizer_ = self.speech_client_.get_recognizer(name=
            self.speech_params_.full_recognizer_path())
    except exceptions.NotFound as ex:
        need_to_create_recognizer = True
    except Exception as generic_ex:
        raise generic_ex


    # Create a Recognizer if it doesn't exist.
    if need_to_create_recognizer:
        print(f'Creating Recognizer ({self.speech_params_.full_recognizer_path()})')
        request = cloud_speech.CreateRecognizerRequest(
            parent=self.speech_params_.base_recognizer_path(),
            recognizer_id=self.speech_params_.recognizer_id,
            recognizer=cloud_speech.Recognizer(
                language_codes=[self.speech_params_.locale],
                model=self.speech_params_.model,
            ),
        )
        operation = self.speech_client_.create_recognizer(request=request)
        self.recognizer_ = operation.result()
        print(f'Recognizer {self.speech_params_.full_recognizer_path()} created.')
        return
    print('No need to create Recognizer '
          f'({self.speech_params_.full_recognizer_path()}). It already exists: ')

  def Recognize(self, audio_file: str) -> cloud_speech.RecognizeResponse:
    """Calls Speech-to-Text Recognize with audio provided.

      Args: (string) audio_file: Audio file local path, or GCS URI to transcribe.
      Returns: cloud_speech.RecognizeResponse
    """
    recognition_config = cloud_speech.RecognitionConfig(auto_decoding_config={})
    recognition_request = cloud_speech.RecognizeRequest(
        recognizer=self.speech_params_.full_recognizer_path(),
        config=recognition_config)
    if audio_file.startswith('gs://'):
        recognition_request.uri = audio_file
    else:
        with io.open(audio_file, "rb") as f:
            recognition_request.content = f.read()

    # Transcribes the audio into text
    response = self.speech_client_.recognize(request=recognition_request)
    return response

def transcribe_file(speech, file_name):
    """
    Transcribe a short audio file using synchronous speech recognition
    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    # Transcribes the audio into text
    response = speech.Recognize(file_name)
    rec_text = ''
    for result in response.results:
        rec_text += result.alternatives[0].transcript
    return rec_text

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("rest_api.py <in_scp> <out_trans>\n")
        exit(-1)

    SCP = sys.argv[1]
    TRANS = sys.argv[2]

    speech = SpeechInterface(SpeechParameters())
    # speech.CreateRecognizer()


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

        rec_text = transcribe_file(speech, audio)

        trans_file.write(key + '\t' + rec_text + '\n')
        trans_file.flush()
        n += 1

    scp_file.close()
    trans_file.close()

