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
from openapi_client.models.line_resource import LineResource  # noqa: E501
from openapi_client.rest import ApiException

class TestLineResource(unittest.TestCase):
    """LineResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LineResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.line_resource.LineResource()  # noqa: E501
        if include_optional :
            return LineResource(
                type = '0', 
                relationships = openapi_client.models.relationships.relationships(), 
                links = openapi_client.models.links.links(), 
                id = '0', 
                attributes = openapi_client.models.line_resource_attributes.LineResource_attributes(
                    text_color = '000000', 
                    sort_order = 56, 
                    short_name = 'CT2', 
                    long_name = 'Sullivan - Ruggles', 
                    color = 'FFFFFF', )
            )
        else :
            return LineResource(
        )

    def testLineResource(self):
        """Test LineResource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
