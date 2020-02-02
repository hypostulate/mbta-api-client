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
from openapi_client.models.trip_resource_attributes import TripResourceAttributes  # noqa: E501
from openapi_client.rest import ApiException

class TestTripResourceAttributes(unittest.TestCase):
    """TripResourceAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TripResourceAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.trip_resource_attributes.TripResourceAttributes()  # noqa: E501
        if include_optional :
            return TripResourceAttributes(
                wheelchair_accessible = 1, 
                name = '596', 
                headsign = 'Harvard', 
                direction_id = 56, 
                block_id = '1070', 
                bikes_allowed = 1
            )
        else :
            return TripResourceAttributes(
        )

    def testTripResourceAttributes(self):
        """Test TripResourceAttributes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
