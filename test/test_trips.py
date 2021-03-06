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
from openapi_client.models.trips import Trips  # noqa: E501
from openapi_client.rest import ApiException

class TestTrips(unittest.TestCase):
    """Trips unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Trips
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.trips.Trips()  # noqa: E501
        if include_optional :
            return Trips(
                links = openapi_client.models.schedules_links.Schedules_links(
                    self = '0', 
                    prev = '0', 
                    next = '0', 
                    last = '0', 
                    first = '0', ), 
                data = [
                    openapi_client.models.trip_resource.TripResource(
                        type = '0', 
                        relationships = openapi_client.models.trip_resource_relationships.TripResource_relationships(
                            shape = openapi_client.models.trip_resource_relationships_shape.TripResource_relationships_shape(
                                links = openapi_client.models.trip_resource_relationships_shape_links.TripResource_relationships_shape_links(
                                    self = '0', 
                                    related = '0', ), 
                                data = openapi_client.models.trip_resource_relationships_shape_data.TripResource_relationships_shape_data(
                                    type = '0', 
                                    id = '0', ), ), 
                            service = openapi_client.models.trip_resource_relationships_service.TripResource_relationships_service(), 
                            route_pattern = openapi_client.models.trip_resource_relationships_route_pattern.TripResource_relationships_route_pattern(), 
                            route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(), ), 
                        links = openapi_client.models.links.links(), 
                        id = '0', 
                        attributes = openapi_client.models.trip_resource_attributes.TripResource_attributes(
                            wheelchair_accessible = 1, 
                            name = '596', 
                            headsign = 'Harvard', 
                            direction_id = 56, 
                            block_id = '1070', 
                            bikes_allowed = 1, ), )
                    ]
            )
        else :
            return Trips(
                data = [
                    openapi_client.models.trip_resource.TripResource(
                        type = '0', 
                        relationships = openapi_client.models.trip_resource_relationships.TripResource_relationships(
                            shape = openapi_client.models.trip_resource_relationships_shape.TripResource_relationships_shape(
                                links = openapi_client.models.trip_resource_relationships_shape_links.TripResource_relationships_shape_links(
                                    self = '0', 
                                    related = '0', ), 
                                data = openapi_client.models.trip_resource_relationships_shape_data.TripResource_relationships_shape_data(
                                    type = '0', 
                                    id = '0', ), ), 
                            service = openapi_client.models.trip_resource_relationships_service.TripResource_relationships_service(), 
                            route_pattern = openapi_client.models.trip_resource_relationships_route_pattern.TripResource_relationships_route_pattern(), 
                            route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(), ), 
                        links = openapi_client.models.links.links(), 
                        id = '0', 
                        attributes = openapi_client.models.trip_resource_attributes.TripResource_attributes(
                            wheelchair_accessible = 1, 
                            name = '596', 
                            headsign = 'Harvard', 
                            direction_id = 56, 
                            block_id = '1070', 
                            bikes_allowed = 1, ), )
                    ],
        )

    def testTrips(self):
        """Test Trips"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
