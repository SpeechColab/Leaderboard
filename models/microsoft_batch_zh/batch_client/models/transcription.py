# coding: utf-8

"""
    Speech Services API v3.1
"""


import pprint
import six
from batch_client.configuration import Configuration


class Transcription(object):

    swagger_types = {
        'links': 'TranscriptionLinks',
        'properties': 'TranscriptionProperties',
        '_self': 'str',
        'model': 'EntityReference',
        'project': 'EntityReference',
        'dataset': 'EntityReference',
        'content_urls': 'list[str]',
        'content_container_url': 'str',
        'locale': 'str',
        'display_name': 'str',
        'description': 'str',
        'custom_properties': 'dict(str, str)',
        'last_action_date_time': 'datetime',
        'status': 'Status',
        'created_date_time': 'datetime'
    }

    attribute_map = {
        'links': 'links',
        'properties': 'properties',
        '_self': 'self',
        'model': 'model',
        'project': 'project',
        'dataset': 'dataset',
        'content_urls': 'contentUrls',
        'content_container_url': 'contentContainerUrl',
        'locale': 'locale',
        'display_name': 'displayName',
        'description': 'description',
        'custom_properties': 'customProperties',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status',
        'created_date_time': 'createdDateTime'
    }

    def __init__(self, links=None, properties=None, _self=None, model=None, project=None, dataset=None, content_urls=None, content_container_url=None, locale=None, display_name=None, description=None, custom_properties=None, last_action_date_time=None, status=None, created_date_time=None, _configuration=None):
        """Transcription - a model defined in Swagger"""
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._links = None
        self._properties = None
        self.__self = None
        self._model = None
        self._project = None
        self._dataset = None
        self._content_urls = None
        self._content_container_url = None
        self._locale = None
        self._display_name = None
        self._description = None
        self._custom_properties = None
        self._last_action_date_time = None
        self._status = None
        self._created_date_time = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if properties is not None:
            self.properties = properties
        if _self is not None:
            self._self = _self
        if model is not None:
            self.model = model
        if project is not None:
            self.project = project
        if dataset is not None:
            self.dataset = dataset
        if content_urls is not None:
            self.content_urls = content_urls
        if content_container_url is not None:
            self.content_container_url = content_container_url
        self.locale = locale
        self.display_name = display_name
        if description is not None:
            self.description = description
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if last_action_date_time is not None:
            self.last_action_date_time = last_action_date_time
        if status is not None:
            self.status = status
        if created_date_time is not None:
            self.created_date_time = created_date_time

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        self._properties = properties

    @property
    def _self(self):
        return self.__self

    @_self.setter
    def _self(self, _self):
        self.__self = _self

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project):
        self._project = project

    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        self._dataset = dataset

    @property
    def content_urls(self):
        return self._content_urls

    @content_urls.setter
    def content_urls(self, content_urls):
        self._content_urls = content_urls

    @property
    def content_container_url(self):
        return self._content_container_url

    @content_container_url.setter
    def content_container_url(self, content_container_url):
        self._content_container_url = content_container_url

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        if self._configuration.client_side_validation and locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")
        if (self._configuration.client_side_validation and
                locale is not None and len(locale) < 1):
            raise ValueError("Invalid value for `locale`, length must be greater than or equal to `1`")

        self._locale = locale

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")

        self._display_name = display_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def custom_properties(self):
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        self._custom_properties = custom_properties

    @property
    def last_action_date_time(self):
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def created_date_time(self):
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        self._created_date_time = created_date_time

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
        if issubclass(Transcription, dict):
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
        if not isinstance(other, Transcription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transcription):
            return True

        return self.to_dict() != other.to_dict()
