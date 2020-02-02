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


class PredictionResourceAttributes(object):
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
        'status': 'str',
        'direction_id': 'int'
    }

    attribute_map = {
        'status': 'status',
        'direction_id': 'direction_id'
    }

    def __init__(self, status=None, direction_id=None, local_vars_configuration=None):  # noqa: E501
        """PredictionResourceAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._direction_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if direction_id is not None:
            self.direction_id = direction_id

    @property
    def status(self):
        """Gets the status of this PredictionResourceAttributes.  # noqa: E501

        Status of the schedule  # noqa: E501

        :return: The status of this PredictionResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PredictionResourceAttributes.

        Status of the schedule  # noqa: E501

        :param status: The status of this PredictionResourceAttributes.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def direction_id(self):
        """Gets the direction_id of this PredictionResourceAttributes.  # noqa: E501

        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    # noqa: E501

        :return: The direction_id of this PredictionResourceAttributes.  # noqa: E501
        :rtype: int
        """
        return self._direction_id

    @direction_id.setter
    def direction_id(self, direction_id):
        """Sets the direction_id of this PredictionResourceAttributes.

        Direction in which trip is traveling: `0` or `1`.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    # noqa: E501

        :param direction_id: The direction_id of this PredictionResourceAttributes.  # noqa: E501
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
        if not isinstance(other, PredictionResourceAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictionResourceAttributes):
            return True

        return self.to_dict() != other.to_dict()