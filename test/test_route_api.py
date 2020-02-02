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

import openapi_client
from openapi_client.api.route_api import RouteApi  # noqa: E501
from openapi_client.rest import ApiException


class TestRouteApi(unittest.TestCase):
    """RouteApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.route_api.RouteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_web_route_controller_index(self):
        """Test case for api_web_route_controller_index

        """
        pass

    def test_api_web_route_controller_show(self):
        """Test case for api_web_route_controller_show

        """
        pass


if __name__ == '__main__':
    unittest.main()
