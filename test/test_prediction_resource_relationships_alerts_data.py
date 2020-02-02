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
from openapi_client.models.prediction_resource_relationships_alerts_data import PredictionResourceRelationshipsAlertsData  # noqa: E501
from openapi_client.rest import ApiException

class TestPredictionResourceRelationshipsAlertsData(unittest.TestCase):
    """PredictionResourceRelationshipsAlertsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PredictionResourceRelationshipsAlertsData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.prediction_resource_relationships_alerts_data.PredictionResourceRelationshipsAlertsData()  # noqa: E501
        if include_optional :
            return PredictionResourceRelationshipsAlertsData(
                type = '0', 
                id = '0'
            )
        else :
            return PredictionResourceRelationshipsAlertsData(
        )

    def testPredictionResourceRelationshipsAlertsData(self):
        """Test PredictionResourceRelationshipsAlertsData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
