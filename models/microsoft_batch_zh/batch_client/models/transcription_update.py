# coding: utf-8

"""
    Speech Services API v3.1
"""


import pprint
import six
from batch_client.configuration import Configuration


class TranscriptionUpdate(object):

    swagger_types = {
        'project': 'EntityReference',
        'display_name': 'str',
        'description': 'str',
        'custom_properties': 'dict(str, str)'
    }

    attribute_map = {
        'project': 'project',
        'display_name': 'displayName',
        'description': 'description',
        'custom_properties': 'customProperties'
    }

    def __init__(self, project=None, display_name=None, description=None, custom_properties=None, _configuration=None):
        """TranscriptionUpdate - a model defined in Swagger"""
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project = None
        self._display_name = None
        self._description = None
        self._custom_properties = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project):
        self._project = project

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
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
        if issubclass(TranscriptionUpdate, dict):
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
        if not isinstance(other, TranscriptionUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranscriptionUpdate):
            return True

        return self.to_dict() != other.to_dict()
