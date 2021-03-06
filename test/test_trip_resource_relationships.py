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
from openapi_client.models.trip_resource_relationships import TripResourceRelationships  # noqa: E501
from openapi_client.rest import ApiException

class TestTripResourceRelationships(unittest.TestCase):
    """TripResourceRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TripResourceRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.trip_resource_relationships.TripResourceRelationships()  # noqa: E501
        if include_optional :
            return TripResourceRelationships(
                shape = openapi_client.models.trip_resource_relationships_shape.TripResource_relationships_shape(
                    links = openapi_client.models.trip_resource_relationships_shape_links.TripResource_relationships_shape_links(
                        self = '0', 
                        related = '0', ), 
                    data = openapi_client.models.trip_resource_relationships_shape_data.TripResource_relationships_shape_data(
                        type = '0', 
                        id = '0', ), ), 
                service = openapi_client.models.trip_resource_relationships_service.TripResource_relationships_service(
                    links = openapi_client.models.trip_resource_relationships_service_links.TripResource_relationships_service_links(
                        self = '0', 
                        related = '0', ), 
                    data = openapi_client.models.trip_resource_relationships_service_data.TripResource_relationships_service_data(
                        type = '0', 
                        id = '0', ), ), 
                route_pattern = openapi_client.models.trip_resource_relationships_route_pattern.TripResource_relationships_route_pattern(
                    links = openapi_client.models.trip_resource_relationships_route_pattern_links.TripResource_relationships_route_pattern_links(
                        self = '0', 
                        related = '0', ), 
                    data = openapi_client.models.trip_resource_relationships_route_pattern_data.TripResource_relationships_route_pattern_data(
                        type = '0', 
                        id = '0', ), ), 
                route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(
                    links = openapi_client.models.prediction_resource_relationships_route_links.PredictionResource_relationships_route_links(
                        self = '0', 
                        related = '0', ), 
                    data = openapi_client.models.prediction_resource_relationships_route_data.PredictionResource_relationships_route_data(
                        type = '0', 
                        id = '0', ), )
            )
        else :
            return TripResourceRelationships(
        )

    def testTripResourceRelationships(self):
        """Test TripResourceRelationships"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
