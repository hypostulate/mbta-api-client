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
from openapi_client.models.shape_resource_relationships_stops import ShapeResourceRelationshipsStops  # noqa: E501
from openapi_client.rest import ApiException

class TestShapeResourceRelationshipsStops(unittest.TestCase):
    """ShapeResourceRelationshipsStops unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ShapeResourceRelationshipsStops
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shape_resource_relationships_stops.ShapeResourceRelationshipsStops()  # noqa: E501
        if include_optional :
            return ShapeResourceRelationshipsStops(
                links = openapi_client.models.shape_resource_relationships_stops_links.ShapeResource_relationships_stops_links(
                    self = '0', 
                    related = '0', ), 
                data = [
                    openapi_client.models.shape_resource_relationships_stops_data.ShapeResource_relationships_stops_data(
                        type = '0', 
                        id = '0', )
                    ]
            )
        else :
            return ShapeResourceRelationshipsStops(
        )

    def testShapeResourceRelationshipsStops(self):
        """Test ShapeResourceRelationshipsStops"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
