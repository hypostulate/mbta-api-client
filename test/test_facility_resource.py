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
from openapi_client.models.facility_resource import FacilityResource  # noqa: E501
from openapi_client.rest import ApiException

class TestFacilityResource(unittest.TestCase):
    """FacilityResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FacilityResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.facility_resource.FacilityResource()  # noqa: E501
        if include_optional :
            return FacilityResource(
                type = '0', 
                relationships = openapi_client.models.facility_resource_relationships.FacilityResource_relationships(
                    stop = openapi_client.models.prediction_resource_relationships_stop.PredictionResource_relationships_stop(
                        links = openapi_client.models.prediction_resource_relationships_stop_links.PredictionResource_relationships_stop_links(
                            self = '0', 
                            related = '0', ), 
                        data = openapi_client.models.prediction_resource_relationships_stop_data.PredictionResource_relationships_stop_data(
                            type = '0', 
                            id = '0', ), ), ), 
                links = openapi_client.models.links.links(), 
                id = '0', 
                attributes = openapi_client.models.facility_resource_attributes.FacilityResource_attributes(
                    type = 'ELEVATOR', 
                    short_name = 'Ashmont platform to lobby', 
                    properties = [
                        {value=197 Ivory St, Braintree, MA 02184, name=address}
                        ], 
                    longitude = 42.316115, 
                    long_name = 'SHAWMUT - Ashmont Bound Platform to Lobby', 
                    latitude = -71.194994, )
            )
        else :
            return FacilityResource(
        )

    def testFacilityResource(self):
        """Test FacilityResource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
