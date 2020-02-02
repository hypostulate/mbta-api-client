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


class Line(object):
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
        'links': 'ServiceLinks',
        'included': 'list[ServiceIncluded]',
        'data': 'LineResource'
    }

    attribute_map = {
        'links': 'links',
        'included': 'included',
        'data': 'data'
    }

    def __init__(self, links=None, included=None, data=None, local_vars_configuration=None):  # noqa: E501
        """Line - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._links = None
        self._included = None
        self._data = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if included is not None:
            self.included = included
        self.data = data

    @property
    def links(self):
        """Gets the links of this Line.  # noqa: E501


        :return: The links of this Line.  # noqa: E501
        :rtype: ServiceLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Line.


        :param links: The links of this Line.  # noqa: E501
        :type: ServiceLinks
        """

        self._links = links

    @property
    def included(self):
        """Gets the included of this Line.  # noqa: E501

        Included resources  # noqa: E501

        :return: The included of this Line.  # noqa: E501
        :rtype: list[ServiceIncluded]
        """
        return self._included

    @included.setter
    def included(self, included):
        """Sets the included of this Line.

        Included resources  # noqa: E501

        :param included: The included of this Line.  # noqa: E501
        :type: list[ServiceIncluded]
        """

        self._included = included

    @property
    def data(self):
        """Gets the data of this Line.  # noqa: E501


        :return: The data of this Line.  # noqa: E501
        :rtype: LineResource
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Line.


        :param data: The data of this Line.  # noqa: E501
        :type: LineResource
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, Line):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Line):
            return True

        return self.to_dict() != other.to_dict()
