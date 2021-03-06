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
from openapi_client.models.predictions import Predictions  # noqa: E501
from openapi_client.rest import ApiException

class TestPredictions(unittest.TestCase):
    """Predictions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Predictions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.predictions.Predictions()  # noqa: E501
        if include_optional :
            return Predictions(
                links = openapi_client.models.schedules_links.Schedules_links(
                    self = '0', 
                    prev = '0', 
                    next = '0', 
                    last = '0', 
                    first = '0', ), 
                data = [
                    openapi_client.models.prediction_resource.PredictionResource(
                        type = '0', 
                        relationships = openapi_client.models.prediction_resource_relationships.PredictionResource_relationships(
                            vehicle = openapi_client.models.prediction_resource_relationships_vehicle.PredictionResource_relationships_vehicle(
                                links = openapi_client.models.prediction_resource_relationships_vehicle_links.PredictionResource_relationships_vehicle_links(
                                    self = '0', 
                                    related = '0', ), 
                                data = openapi_client.models.prediction_resource_relationships_vehicle_data.PredictionResource_relationships_vehicle_data(
                                    type = '0', 
                                    id = '0', ), ), 
                            trip = openapi_client.models.prediction_resource_relationships_trip.PredictionResource_relationships_trip(), 
                            stop = openapi_client.models.prediction_resource_relationships_stop.PredictionResource_relationships_stop(), 
                            schedule = openapi_client.models.prediction_resource_relationships_schedule.PredictionResource_relationships_schedule(), 
                            route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(), 
                            alerts = openapi_client.models.prediction_resource_relationships_alerts.PredictionResource_relationships_alerts(), ), 
                        links = openapi_client.models.links.links(), 
                        id = '0', 
                        attributes = openapi_client.models.prediction_resource_attributes.PredictionResource_attributes(
                            status = 'Approaching', 
                            direction_id = 56, ), )
                    ]
            )
        else :
            return Predictions(
                data = [
                    openapi_client.models.prediction_resource.PredictionResource(
                        type = '0', 
                        relationships = openapi_client.models.prediction_resource_relationships.PredictionResource_relationships(
                            vehicle = openapi_client.models.prediction_resource_relationships_vehicle.PredictionResource_relationships_vehicle(
                                links = openapi_client.models.prediction_resource_relationships_vehicle_links.PredictionResource_relationships_vehicle_links(
                                    self = '0', 
                                    related = '0', ), 
                                data = openapi_client.models.prediction_resource_relationships_vehicle_data.PredictionResource_relationships_vehicle_data(
                                    type = '0', 
                                    id = '0', ), ), 
                            trip = openapi_client.models.prediction_resource_relationships_trip.PredictionResource_relationships_trip(), 
                            stop = openapi_client.models.prediction_resource_relationships_stop.PredictionResource_relationships_stop(), 
                            schedule = openapi_client.models.prediction_resource_relationships_schedule.PredictionResource_relationships_schedule(), 
                            route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(), 
                            alerts = openapi_client.models.prediction_resource_relationships_alerts.PredictionResource_relationships_alerts(), ), 
                        links = openapi_client.models.links.links(), 
                        id = '0', 
                        attributes = openapi_client.models.prediction_resource_attributes.PredictionResource_attributes(
                            status = 'Approaching', 
                            direction_id = 56, ), )
                    ],
        )

    def testPredictions(self):
        """Test Predictions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
