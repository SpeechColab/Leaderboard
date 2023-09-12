# coding: utf-8

"""
    Speech Services API v3.1
"""


import pprint
import six
from batch_client.configuration import Configuration


class TranscriptionProperties(object):

    swagger_types = {
        'diarization_enabled': 'bool',
        'word_level_timestamps_enabled': 'bool',
        'display_form_word_level_timestamps_enabled': 'bool',
        'duration': 'str',
        'channels': 'list[int]',
        'destination_container_url': 'str',
        'punctuation_mode': 'PunctuationMode',
        'profanity_filter_mode': 'ProfanityFilterMode',
        'time_to_live': 'str',
        'diarization': 'DiarizationProperties',
        'language_identification': 'LanguageIdentificationProperties',
        'email': 'str',
        'error': 'EntityError'
    }

    attribute_map = {
        'diarization_enabled': 'diarizationEnabled',
        'word_level_timestamps_enabled': 'wordLevelTimestampsEnabled',
        'display_form_word_level_timestamps_enabled': 'displayFormWordLevelTimestampsEnabled',
        'duration': 'duration',
        'channels': 'channels',
        'destination_container_url': 'destinationContainerUrl',
        'punctuation_mode': 'punctuationMode',
        'profanity_filter_mode': 'profanityFilterMode',
        'time_to_live': 'timeToLive',
        'diarization': 'diarization',
        'language_identification': 'languageIdentification',
        'email': 'email',
        'error': 'error'
    }

    def __init__(self, diarization_enabled=None, word_level_timestamps_enabled=None, display_form_word_level_timestamps_enabled=None, duration=None, channels=None, destination_container_url=None, punctuation_mode=None, profanity_filter_mode=None, time_to_live=None, diarization=None, language_identification=None, email=None, error=None, _configuration=None):
        """TranscriptionProperties - a model defined in Swagger"""
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diarization_enabled = None
        self._word_level_timestamps_enabled = None
        self._display_form_word_level_timestamps_enabled = None
        self._duration = None
        self._channels = None
        self._destination_container_url = None
        self._punctuation_mode = None
        self._profanity_filter_mode = None
        self._time_to_live = None
        self._diarization = None
        self._language_identification = None
        self._email = None
        self._error = None
        self.discriminator = None

        if diarization_enabled is not None:
            self.diarization_enabled = diarization_enabled
        if word_level_timestamps_enabled is not None:
            self.word_level_timestamps_enabled = word_level_timestamps_enabled
        if display_form_word_level_timestamps_enabled is not None:
            self.display_form_word_level_timestamps_enabled = display_form_word_level_timestamps_enabled
        if duration is not None:
            self.duration = duration
        if channels is not None:
            self.channels = channels
        if destination_container_url is not None:
            self.destination_container_url = destination_container_url
        if punctuation_mode is not None:
            self.punctuation_mode = punctuation_mode
        if profanity_filter_mode is not None:
            self.profanity_filter_mode = profanity_filter_mode
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if diarization is not None:
            self.diarization = diarization
        if language_identification is not None:
            self.language_identification = language_identification
        if email is not None:
            self.email = email
        if error is not None:
            self.error = error

    @property
    def diarization_enabled(self):
        return self._diarization_enabled

    @diarization_enabled.setter
    def diarization_enabled(self, diarization_enabled):
        self._diarization_enabled = diarization_enabled

    @property
    def word_level_timestamps_enabled(self):
        return self._word_level_timestamps_enabled

    @word_level_timestamps_enabled.setter
    def word_level_timestamps_enabled(self, word_level_timestamps_enabled):
        self._word_level_timestamps_enabled = word_level_timestamps_enabled

    @property
    def display_form_word_level_timestamps_enabled(self):
        return self._display_form_word_level_timestamps_enabled

    @display_form_word_level_timestamps_enabled.setter
    def display_form_word_level_timestamps_enabled(self, display_form_word_level_timestamps_enabled):
        self._display_form_word_level_timestamps_enabled = display_form_word_level_timestamps_enabled

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels):
        self._channels = channels

    @property
    def destination_container_url(self):
        return self._destination_container_url

    @destination_container_url.setter
    def destination_container_url(self, destination_container_url):
        self._destination_container_url = destination_container_url

    @property
    def punctuation_mode(self):
        return self._punctuation_mode

    @punctuation_mode.setter
    def punctuation_mode(self, punctuation_mode):
        self._punctuation_mode = punctuation_mode

    @property
    def profanity_filter_mode(self):
        return self._profanity_filter_mode

    @profanity_filter_mode.setter
    def profanity_filter_mode(self, profanity_filter_mode):
        self._profanity_filter_mode = profanity_filter_mode

    @property
    def time_to_live(self):
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        self._time_to_live = time_to_live

    @property
    def diarization(self):
        return self._diarization

    @diarization.setter
    def diarization(self, diarization):
        self._diarization = diarization

    @property
    def language_identification(self):
        return self._language_identification

    @language_identification.setter
    def language_identification(self, language_identification):
        self._language_identification = language_identification

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TranscriptionProperties, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TranscriptionProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranscriptionProperties):
            return True

        return self.to_dict() != other.to_dict()
