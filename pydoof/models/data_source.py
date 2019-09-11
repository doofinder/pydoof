# coding: utf-8

"""
    Doofinder API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@doofinder.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pydoof.models.update_data_source import UpdateDataSource  # noqa: F401,E501


class DataSource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'options': 'object',
        'type': 'str',
        'item_processors': 'list[ERRORUNKNOWN]'
    }

    attribute_map = {
        'url': 'url',
        'options': 'options',
        'type': 'type',
        'item_processors': 'item_processors'
    }

    def __init__(self, url=None, options=None, type=None, item_processors=None):  # noqa: E501
        """DataSource - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._options = None
        self._type = None
        self._item_processors = None
        self.discriminator = None

        self.url = url
        if options is not None:
            self.options = options
        self.type = type
        if item_processors is not None:
            self.item_processors = item_processors

    @property
    def url(self):
        """Gets the url of this DataSource.  # noqa: E501

        Source of the data feed  # noqa: E501

        :return: The url of this DataSource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DataSource.

        Source of the data feed  # noqa: E501

        :param url: The url of this DataSource.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def options(self):
        """Gets the options of this DataSource.  # noqa: E501

        Options of the datasource  # noqa: E501

        :return: The options of this DataSource.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DataSource.

        Options of the datasource  # noqa: E501

        :param options: The options of this DataSource.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def type(self):
        """Gets the type of this DataSource.  # noqa: E501

        Type of the datasource. One of (file, shopify)  # noqa: E501

        :return: The type of this DataSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataSource.

        Type of the datasource. One of (file, shopify)  # noqa: E501

        :param type: The type of this DataSource.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["file", "shopify"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def item_processors(self):
        """Gets the item_processors of this DataSource.  # noqa: E501

        Custom items processors  # noqa: E501

        :return: The item_processors of this DataSource.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._item_processors

    @item_processors.setter
    def item_processors(self, item_processors):
        """Sets the item_processors of this DataSource.

        Custom items processors  # noqa: E501

        :param item_processors: The item_processors of this DataSource.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._item_processors = item_processors

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
        if issubclass(DataSource, dict):
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
        if not isinstance(other, DataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
