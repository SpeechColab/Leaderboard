# coding: utf-8

"""
    Speech Services API v3.1
"""


from __future__ import absolute_import

# import apis into sdk package
from batch_client.api.custom_speech_transcriptions_api import CustomSpeechTranscriptionsApi

# import ApiClient
from batch_client.api_client import ApiClient
from batch_client.configuration import Configuration

# import models into sdk package
from batch_client.models.transcription import Transcription
from batch_client.models.transcription_links import TranscriptionLinks
from batch_client.models.transcription_properties import TranscriptionProperties
from batch_client.models.transcription_update import TranscriptionUpdate
