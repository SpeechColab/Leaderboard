# coding: utf-8

"""
    Speech Services API v3.1
"""


import pprint
import six
from batch_client.configuration import Configuration


class PaginatedFiles(object):

    swagger_types = {
        'values': 'list[File]',
        'next_link': 'str'
    }

    attribute_map = {
        'values': 'values',
        'next_link': '@nextLink'
    }

    def __init__(self, values=None, next_link=None, _configuration=None):
        """PaginatedFiles - a model defined in Swagger"""
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._values = None
        self._next_link = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if next_link is not None:
            self.next_link = next_link

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values

    @property
    def next_link(self):
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        self._next_link = next_link

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
        if issubclass(PaginatedFiles, dict):
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
        if not isinstance(other, PaginatedFiles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginatedFiles):
            return True

        return self.to_dict() != other.to_dict()
