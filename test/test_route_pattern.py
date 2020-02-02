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
from openapi_client.models.route_pattern import RoutePattern  # noqa: E501
from openapi_client.rest import ApiException

class TestRoutePattern(unittest.TestCase):
    """RoutePattern unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoutePattern
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.route_pattern.RoutePattern()  # noqa: E501
        if include_optional :
            return RoutePattern(
                links = openapi_client.models.service_links.Service_links(
                    self = '0', ), 
                included = [
                    openapi_client.models.service_included.Service_included(
                        type = '0', 
                        id = '0', )
                    ], 
                data = openapi_client.models.route_pattern_resource.RoutePatternResource(
                    type = '0', 
                    relationships = openapi_client.models.route_pattern_resource_relationships.RoutePatternResource_relationships(
                        route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(
                            links = openapi_client.models.prediction_resource_relationships_route_links.PredictionResource_relationships_route_links(
                                self = '0', 
                                related = '0', ), 
                            data = openapi_client.models.prediction_resource_relationships_route_data.PredictionResource_relationships_route_data(
                                type = '0', 
                                id = '0', ), ), 
                        representative_trip = openapi_client.models.route_pattern_resource_relationships_representative_trip.RoutePatternResource_relationships_representative_trip(), ), 
                    links = openapi_client.models.links.links(), 
                    id = '0', 
                    attributes = openapi_client.models.route_pattern_resource_attributes.RoutePatternResource_attributes(
                        typicality = 56, 
                        sort_order = 56, 
                        name = 'Forge Park/495 - South Station via Fairmount', 
                        direction_id = 56, ), )
            )
        else :
            return RoutePattern(
                data = openapi_client.models.route_pattern_resource.RoutePatternResource(
                    type = '0', 
                    relationships = openapi_client.models.route_pattern_resource_relationships.RoutePatternResource_relationships(
                        route = openapi_client.models.prediction_resource_relationships_route.PredictionResource_relationships_route(
                            links = openapi_client.models.prediction_resource_relationships_route_links.PredictionResource_relationships_route_links(
                                self = '0', 
                                related = '0', ), 
                            data = openapi_client.models.prediction_resource_relationships_route_data.PredictionResource_relationships_route_data(
                                type = '0', 
                                id = '0', ), ), 
                        representative_trip = openapi_client.models.route_pattern_resource_relationships_representative_trip.RoutePatternResource_relationships_representative_trip(), ), 
                    links = openapi_client.models.links.links(), 
                    id = '0', 
                    attributes = openapi_client.models.route_pattern_resource_attributes.RoutePatternResource_attributes(
                        typicality = 56, 
                        sort_order = 56, 
                        name = 'Forge Park/495 - South Station via Fairmount', 
                        direction_id = 56, ), ),
        )

    def testRoutePattern(self):
        """Test RoutePattern"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
