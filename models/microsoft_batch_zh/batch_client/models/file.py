# coding: utf-8

"""
    Speech Services API v3.1
"""


import pprint
import six
from batch_client.configuration import Configuration


class File(object):

    swagger_types = {
        'kind': 'FileKind',
        'links': 'FileLinks',
        'created_date_time': 'datetime',
        'properties': 'FileProperties',
        'name': 'str',
        '_self': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'links': 'links',
        'created_date_time': 'createdDateTime',
        'properties': 'properties',
        'name': 'name',
        '_self': 'self'
    }

    def __init__(self, kind=None, links=None, created_date_time=None, properties=None, name=None, _self=None, _configuration=None):
        """File - a model defined in Swagger"""
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._kind = None
        self._links = None
        self._created_date_time = None
        self._properties = None
        self._name = None
        self.__self = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if links is not None:
            self.links = links
        if created_date_time is not None:
            self.created_date_time = created_date_time
        if properties is not None:
            self.properties = properties
        if name is not None:
            self.name = name
        if _self is not None:
            self._self = _self

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def created_date_time(self):
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        self._created_date_time = created_date_time

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        self._properties = properties

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def _self(self):
        return self.__self

    @_self.setter
    def _self(self, _self):
        self.__self = _self

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
        if issubclass(File, dict):
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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
