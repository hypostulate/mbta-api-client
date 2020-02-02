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
from openapi_client.models.bad_request import BadRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestBadRequest(unittest.TestCase):
    """BadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BadRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.bad_request.BadRequest()  # noqa: E501
        if include_optional :
            return BadRequest(
                errors = [
                    openapi_client.models.bad_request_errors.BadRequest_errors(
                        status = '400', 
                        source = openapi_client.models.bad_request_source.BadRequest_source(
                            parameter = 'sort', ), 
                        detail = 'Invalid sort key', 
                        code = 'bad_request', )
                    ]
            )
        else :
            return BadRequest(
                errors = [
                    openapi_client.models.bad_request_errors.BadRequest_errors(
                        status = '400', 
                        source = openapi_client.models.bad_request_source.BadRequest_source(
                            parameter = 'sort', ), 
                        detail = 'Invalid sort key', 
                        code = 'bad_request', )
                    ],
        )

    def testBadRequest(self):
        """Test BadRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
