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
from openapi_client.models.service import Service  # noqa: E501
from openapi_client.rest import ApiException

class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Service
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.service.Service()  # noqa: E501
        if include_optional :
            return Service(
                links = openapi_client.models.service_links.Service_links(
                    self = '0', ), 
                included = [
                    openapi_client.models.service_included.Service_included(
                        type = '0', 
                        id = '0', )
                    ], 
                data = openapi_client.models.service_resource.ServiceResource(
                    type = '0', 
                    relationships = openapi_client.models.relationships.relationships(), 
                    links = openapi_client.models.links.links(), 
                    id = '0', 
                    attributes = openapi_client.models.service_resource_attributes.ServiceResource_attributes(
                        valid_days = [
                            1.0
                            ], 
                        start_date = 'Mon Nov 19 00:00:00 GMT 2018', 
                        schedule_typicality = 1, 
                        schedule_type = 'Sunday', 
                        schedule_name = 'Weekday (no school)', 
                        removed_dates_notes = [
                            'New Year Day'
                            ], 
                        removed_dates = [
                            'Mon Dec 17 00:00:00 GMT 2018'
                            ], 
                        rating_start_date = 'Sat Dec 22 00:00:00 GMT 2018', 
                        rating_end_date = 'Thu Mar 14 00:00:00 GMT 2019', 
                        rating_description = 'Winter', 
                        end_date = 'Mon Dec 24 00:00:00 GMT 2018', 
                        description = 'Weekday schedule (no school)', 
                        added_dates_notes = [
                            'New Year Day'
                            ], 
                        added_dates = [
                            'Wed Nov 21 00:00:00 GMT 2018'
                            ], ), )
            )
        else :
            return Service(
                data = openapi_client.models.service_resource.ServiceResource(
                    type = '0', 
                    relationships = openapi_client.models.relationships.relationships(), 
                    links = openapi_client.models.links.links(), 
                    id = '0', 
                    attributes = openapi_client.models.service_resource_attributes.ServiceResource_attributes(
                        valid_days = [
                            1.0
                            ], 
                        start_date = 'Mon Nov 19 00:00:00 GMT 2018', 
                        schedule_typicality = 1, 
                        schedule_type = 'Sunday', 
                        schedule_name = 'Weekday (no school)', 
                        removed_dates_notes = [
                            'New Year Day'
                            ], 
                        removed_dates = [
                            'Mon Dec 17 00:00:00 GMT 2018'
                            ], 
                        rating_start_date = 'Sat Dec 22 00:00:00 GMT 2018', 
                        rating_end_date = 'Thu Mar 14 00:00:00 GMT 2019', 
                        rating_description = 'Winter', 
                        end_date = 'Mon Dec 24 00:00:00 GMT 2018', 
                        description = 'Weekday schedule (no school)', 
                        added_dates_notes = [
                            'New Year Day'
                            ], 
                        added_dates = [
                            'Wed Nov 21 00:00:00 GMT 2018'
                            ], ), ),
        )

    def testService(self):
        """Test Service"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
