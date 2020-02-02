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


class ShapeResourceAttributes(object):
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
        'priority': 'int',
        'polyline': 'str',
        'name': 'str',
        'direction_id': 'int'
    }

    attribute_map = {
        'priority': 'priority',
        'polyline': 'polyline',
        'name': 'name',
        'direction_id': 'direction_id'
    }

    def __init__(self, priority=None, polyline=None, name=None, direction_id=None, local_vars_configuration=None):  # noqa: E501
        """ShapeResourceAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._priority = None
        self._polyline = None
        self._name = None
        self._direction_id = None
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if polyline is not None:
            self.polyline = polyline
        if name is not None:
            self.name = name
        if direction_id is not None:
            self.direction_id = direction_id

    @property
    def priority(self):
        """Gets the priority of this ShapeResourceAttributes.  # noqa: E501

        Representation of how important a shape is when choosing one for display. Higher number is higher priority.  Negative priority is not important enough to show as they only **MAY** be used.   # noqa: E501

        :return: The priority of this ShapeResourceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ShapeResourceAttributes.

        Representation of how important a shape is when choosing one for display. Higher number is higher priority.  Negative priority is not important enough to show as they only **MAY** be used.   # noqa: E501

        :param priority: The priority of this ShapeResourceAttributes.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def polyline(self):
        """Gets the polyline of this ShapeResourceAttributes.  # noqa: E501

        ## Encoding/Decoding  [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)  ## Example Libraries  * [Javascript](https://www.npmjs.com/package/polyline) * [Erlang](https://blog.kempkens.io/posts/encoding-and-decoding-polylines-with-erlang/) * [Elixir](https://hex.pm/packages/polyline)   # noqa: E501

        :return: The polyline of this ShapeResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._polyline

    @polyline.setter
    def polyline(self, polyline):
        """Sets the polyline of this ShapeResourceAttributes.

        ## Encoding/Decoding  [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)  ## Example Libraries  * [Javascript](https://www.npmjs.com/package/polyline) * [Erlang](https://blog.kempkens.io/posts/encoding-and-decoding-polylines-with-erlang/) * [Elixir](https://hex.pm/packages/polyline)   # noqa: E501

        :param polyline: The polyline of this ShapeResourceAttributes.  # noqa: E501
        :type: str
        """

        self._polyline = polyline

    @property
    def name(self):
        """Gets the name of this ShapeResourceAttributes.  # noqa: E501

        User-facing name for shape. It may, but is not required to, be a headsign  # noqa: E501

        :return: The name of this ShapeResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShapeResourceAttributes.

        User-facing name for shape. It may, but is not required to, be a headsign  # noqa: E501

        :param name: The name of this ShapeResourceAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def direction_id(self):
        """Gets the direction_id of this ShapeResourceAttributes.  # noqa: E501

        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    # noqa: E501

        :return: The direction_id of this ShapeResourceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._direction_id

    @direction_id.setter
    def direction_id(self, direction_id):
        """Sets the direction_id of this ShapeResourceAttributes.

        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    # noqa: E501

        :param direction_id: The direction_id of this ShapeResourceAttributes.  # noqa: E501
        :type: int
        """

        self._direction_id = direction_id

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
        if not isinstance(other, ShapeResourceAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShapeResourceAttributes):
            return True

        return self.to_dict() != other.to_dict()