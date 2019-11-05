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


class Scroll(object):
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
        'total': 'int',
        'scroll_id': 'str',
        'items': 'Items'
    }

    attribute_map = {
        'total': 'total',
        'scroll_id': 'scroll_id',
        'items': 'items'
    }

    def __init__(self, total=None, scroll_id=None, items=None):  # noqa: E501
        """Scroll - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._scroll_id = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if scroll_id is not None:
            self.scroll_id = scroll_id
        if items is not None:
            self.items = items

    @property
    def total(self):
        """Gets the total of this Scroll.  # noqa: E501

        Total number of items  # noqa: E501

        :return: The total of this Scroll.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Scroll.

        Total number of items  # noqa: E501

        :param total: The total of this Scroll.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def scroll_id(self):
        """Gets the scroll_id of this Scroll.  # noqa: E501

        Unique identifier for the Scroll  # noqa: E501

        :return: The scroll_id of this Scroll.  # noqa: E501
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        """Sets the scroll_id of this Scroll.

        Unique identifier for the Scroll  # noqa: E501

        :param scroll_id: The scroll_id of this Scroll.  # noqa: E501
        :type: str
        """

        self._scroll_id = scroll_id

    @property
    def items(self):
        """Gets the items of this Scroll.  # noqa: E501


        :return: The items of this Scroll.  # noqa: E501
        :rtype: Items
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Scroll.


        :param items: The items of this Scroll.  # noqa: E501
        :type: Items
        """

        self._items = items

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
        if issubclass(Scroll, dict):
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
        if not isinstance(other, Scroll):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
