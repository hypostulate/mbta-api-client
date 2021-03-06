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


class PredictionResourceRelationships(object):
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
        'vehicle': 'PredictionResourceRelationshipsVehicle',
        'trip': 'PredictionResourceRelationshipsTrip',
        'stop': 'PredictionResourceRelationshipsStop',
        'schedule': 'PredictionResourceRelationshipsSchedule',
        'route': 'PredictionResourceRelationshipsRoute',
        'alerts': 'PredictionResourceRelationshipsAlerts'
    }

    attribute_map = {
        'vehicle': 'vehicle',
        'trip': 'trip',
        'stop': 'stop',
        'schedule': 'schedule',
        'route': 'route',
        'alerts': 'alerts'
    }

    def __init__(self, vehicle=None, trip=None, stop=None, schedule=None, route=None, alerts=None, local_vars_configuration=None):  # noqa: E501
        """PredictionResourceRelationships - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vehicle = None
        self._trip = None
        self._stop = None
        self._schedule = None
        self._route = None
        self._alerts = None
        self.discriminator = None

        if vehicle is not None:
            self.vehicle = vehicle
        if trip is not None:
            self.trip = trip
        if stop is not None:
            self.stop = stop
        if schedule is not None:
            self.schedule = schedule
        if route is not None:
            self.route = route
        if alerts is not None:
            self.alerts = alerts

    @property
    def vehicle(self):
        """Gets the vehicle of this PredictionResourceRelationships.  # noqa: E501


        :return: The vehicle of this PredictionResourceRelationships.  # noqa: E501
        :rtype: PredictionResourceRelationshipsVehicle
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this PredictionResourceRelationships.


        :param vehicle: The vehicle of this PredictionResourceRelationships.  # noqa: E501
        :type: PredictionResourceRelationshipsVehicle
        """

        self._vehicle = vehicle

    @property
    def trip(self):
        """Gets the trip of this PredictionResourceRelationships.  # noqa: E501


        :return: The trip of this PredictionResourceRelationships.  # noqa: E501
        :rtype: PredictionResourceRelationshipsTrip
        """
        return self._trip

    @trip.setter
    def trip(self, trip):
        """Sets the trip of this PredictionResourceRelationships.


        :param trip: The trip of this PredictionResourceRelationships.  # noqa: E501
        :type: PredictionResourceRelationshipsTrip
        """

        self._trip = trip

    @property
    def stop(self):
        """Gets the stop of this PredictionResourceRelationships.  # noqa: E501


        :return: The stop of this PredictionResourceRelationships.  # noqa: E501
        :rtype: PredictionResourceRelationshipsStop
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this PredictionResourceRelationships.


        :param stop: The stop of this PredictionResourceRelationships.  # noqa: E501
        :type: PredictionResourceRelationshipsStop
        """

        self._stop = stop

    @property
    def schedule(self):
        """Gets the schedule of this PredictionResourceRelationships.  # noqa: E501


        :return: The schedule of this PredictionResourceRelationships.  # noqa: E501
        :rtype: PredictionResourceRelationshipsSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this PredictionResourceRelationships.


        :param schedule: The schedule of this PredictionResourceRelationships.  # noqa: E501
        :type: PredictionResourceRelationshipsSchedule
        """

        self._schedule = schedule

    @property
    def route(self):
        """Gets the route of this PredictionResourceRelationships.  # noqa: E501


        :return: The route of this PredictionResourceRelationships.  # noqa: E501
        :rtype: PredictionResourceRelationshipsRoute
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this PredictionResourceRelationships.


        :param route: The route of this PredictionResourceRelationships.  # noqa: E501
        :type: PredictionResourceRelationshipsRoute
        """

        self._route = route

    @property
    def alerts(self):
        """Gets the alerts of this PredictionResourceRelationships.  # noqa: E501


        :return: The alerts of this PredictionResourceRelationships.  # noqa: E501
        :rtype: PredictionResourceRelationshipsAlerts
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this PredictionResourceRelationships.


        :param alerts: The alerts of this PredictionResourceRelationships.  # noqa: E501
        :type: PredictionResourceRelationshipsAlerts
        """

        self._alerts = alerts

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
        if not isinstance(other, PredictionResourceRelationships):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PredictionResourceRelationships):
            return True

        return self.to_dict() != other.to_dict()
