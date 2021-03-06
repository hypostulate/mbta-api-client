# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com Source code: https://github.com/mbta/api  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: developer@mbta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.schedules import Schedules  # noqa: E501
from openapi_client.rest import ApiException

class TestSchedules(unittest.TestCase):
    """Schedules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Schedules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.schedules.Schedules()  # noqa: E501
        if include_optional :
            return Schedules(
                links = openapi_client.models.schedules_links.Schedules_links(
                    self = '0', 
                    prev = '0', 
                    next = '0', 
                    last = '0', 
                    first = '0', ), 
                data = [
                    openapi_client.models.schedule_resource.ScheduleResource(
                        type = '0', 
                        relationships = openapi_client.models.schedule_resource_relationships.ScheduleResource_relationships(
                            trip = openapi_client.models.prediction_resource_relationships_trip.PredictionResource_relationships_trip(
                                links = openapi_client.models.prediction_resource_relationships_trip_links.PredictionResource_relationships_trip_links(
                                    self = '0', 
                                    related = '0', ), 
                                data = openapi_client.models.prediction_resource_relationships_trip_data.PredictionResource_relationships_trip_data(
                                    type = '0', 
                                    id = '0', ), ), 
                            stop = openapi_client.models.prediction_resource_relationships_stop.PredictionResource_relationships_stop(), 
                            route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(), 
                            prediction = openapi_client.models.schedule_resource_relationships_prediction.ScheduleResource_relationships_prediction(), ), 
                        links = openapi_client.models.links.links(), 
                        id = '0', 
                        attributes = openapi_client.models.schedule_resource_attributes.ScheduleResource_attributes(
                            timepoint = False, 
                            stop_sequence = 1, 
                            pickup_type = 0, 
                            drop_off_type = 1, 
                            direction_id = 56, 
                            departure_time = '2017-08-14T15:04-04:00', 
                            arrival_time = '2017-08-14T15:04-04:00', ), )
                    ]
            )
        else :
            return Schedules(
                data = [
                    openapi_client.models.schedule_resource.ScheduleResource(
                        type = '0', 
                        relationships = openapi_client.models.schedule_resource_relationships.ScheduleResource_relationships(
                            trip = openapi_client.models.prediction_resource_relationships_trip.PredictionResource_relationships_trip(
                                links = openapi_client.models.prediction_resource_relationships_trip_links.PredictionResource_relationships_trip_links(
                                    self = '0', 
                                    related = '0', ), 
                                data = openapi_client.models.prediction_resource_relationships_trip_data.PredictionResource_relationships_trip_data(
                                    type = '0', 
                                    id = '0', ), ), 
                            stop = openapi_client.models.prediction_resource_relationships_stop.PredictionResource_relationships_stop(), 
                            route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(), 
                            prediction = openapi_client.models.schedule_resource_relationships_prediction.ScheduleResource_relationships_prediction(), ), 
                        links = openapi_client.models.links.links(), 
                        id = '0', 
                        attributes = openapi_client.models.schedule_resource_attributes.ScheduleResource_attributes(
                            timepoint = False, 
                            stop_sequence = 1, 
                            pickup_type = 0, 
                            drop_off_type = 1, 
                            direction_id = 56, 
                            departure_time = '2017-08-14T15:04-04:00', 
                            arrival_time = '2017-08-14T15:04-04:00', ), )
                    ],
        )

    def testSchedules(self):
        """Test Schedules"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
