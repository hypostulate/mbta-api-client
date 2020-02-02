# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com Source code: https://github.com/mbta/api  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: developer@mbta.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class LineResourceAttributes(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'text_color': 'str',
        'sort_order': 'int',
        'short_name': 'str',
        'long_name': 'str',
        'color': 'str'
    }

    attribute_map = {
        'text_color': 'text_color',
        'sort_order': 'sort_order',
        'short_name': 'short_name',
        'long_name': 'long_name',
        'color': 'color'
    }

    def __init__(self, text_color=None, sort_order=None, short_name=None, long_name=None, color=None, local_vars_configuration=None):  # noqa: E501
        """LineResourceAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text_color = None
        self._sort_order = None
        self._short_name = None
        self._long_name = None
        self._color = None
        self.discriminator = None

        if text_color is not None:
            self.text_color = text_color
        if sort_order is not None:
            self.sort_order = sort_order
        if short_name is not None:
            self.short_name = short_name
        if long_name is not None:
            self.long_name = long_name
        if color is not None:
            self.color = color

    @property
    def text_color(self):
        """Gets the text_color of this LineResourceAttributes.  # noqa: E501

        This field can be used to specify a legible color to use for text drawn against a background of line_color. The color must be provided as a six-character hexadecimal number, for example, `FFD700`.   # noqa: E501

        :return: The text_color of this LineResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        """Sets the text_color of this LineResourceAttributes.

        This field can be used to specify a legible color to use for text drawn against a background of line_color. The color must be provided as a six-character hexadecimal number, for example, `FFD700`.   # noqa: E501

        :param text_color: The text_color of this LineResourceAttributes.  # noqa: E501
        :type: str
        """

        self._text_color = text_color

    @property
    def sort_order(self):
        """Gets the sort_order of this LineResourceAttributes.  # noqa: E501

        Lines sort in ascending order  # noqa: E501

        :return: The sort_order of this LineResourceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this LineResourceAttributes.

        Lines sort in ascending order  # noqa: E501

        :param sort_order: The sort_order of this LineResourceAttributes.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def short_name(self):
        """Gets the short_name of this LineResourceAttributes.  # noqa: E501

        Short, public-facing name for the group of routes represented in this line   # noqa: E501

        :return: The short_name of this LineResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this LineResourceAttributes.

        Short, public-facing name for the group of routes represented in this line   # noqa: E501

        :param short_name: The short_name of this LineResourceAttributes.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def long_name(self):
        """Gets the long_name of this LineResourceAttributes.  # noqa: E501

        Lengthier, public-facing name for the group of routes represented in this line   # noqa: E501

        :return: The long_name of this LineResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this LineResourceAttributes.

        Lengthier, public-facing name for the group of routes represented in this line   # noqa: E501

        :param long_name: The long_name of this LineResourceAttributes.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def color(self):
        """Gets the color of this LineResourceAttributes.  # noqa: E501

        In systems that have colors assigned to lines, the route_color field defines a color that corresponds to a line. The color must be provided as a six-character hexadecimal number, for example, `00FFFF`.   # noqa: E501

        :return: The color of this LineResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this LineResourceAttributes.

        In systems that have colors assigned to lines, the route_color field defines a color that corresponds to a line. The color must be provided as a six-character hexadecimal number, for example, `00FFFF`.   # noqa: E501

        :param color: The color of this LineResourceAttributes.  # noqa: E501
        :type: str
        """

        self._color = color

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LineResourceAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LineResourceAttributes):
            return True

        return self.to_dict() != other.to_dict()
