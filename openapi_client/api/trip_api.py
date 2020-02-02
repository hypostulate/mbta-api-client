# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com Source code: https://github.com/mbta/api  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: developer@mbta.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TripApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_web_trip_controller_index(self, **kwargs):  # noqa: E501
        """api_web_trip_controller_index  # noqa: E501

        **NOTE:** A id, route, route_pattern, or name filter **MUST** be present for any trips to be returned.  List of trips, the journies of a particular vehicle through a set of stops on a primary `route` and zero or more alternative `route`s that can be filtered on.  ## Accessibility  Wheelchair accessibility (`/data/{index}/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/{index}/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_trip_controller_index(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bikes_allowed` | ascending | `bikes_allowed` | | `/data/{index}/attributes/bikes_allowed` | descending | `-bikes_allowed` | | `/data/{index}/attributes/block_id` | ascending | `block_id` | | `/data/{index}/attributes/block_id` | descending | `-block_id` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/headsign` | ascending | `headsign` | | `/data/{index}/attributes/headsign` | descending | `-headsign` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/wheelchair_accessible` | ascending | `wheelchair_accessible` | | `/data/{index}/attributes/wheelchair_accessible` | descending | `-wheelchair_accessible` |  
        :param str fields_trip: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |  
        :param date filter_date: Filter by trips on a particular date The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD.
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route_pattern: Filter by route pattern IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_id: Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_name: Filter by multiple names. **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Trips
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_web_trip_controller_index_with_http_info(**kwargs)  # noqa: E501

    def api_web_trip_controller_index_with_http_info(self, **kwargs):  # noqa: E501
        """api_web_trip_controller_index  # noqa: E501

        **NOTE:** A id, route, route_pattern, or name filter **MUST** be present for any trips to be returned.  List of trips, the journies of a particular vehicle through a set of stops on a primary `route` and zero or more alternative `route`s that can be filtered on.  ## Accessibility  Wheelchair accessibility (`/data/{index}/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/{index}/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_trip_controller_index_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bikes_allowed` | ascending | `bikes_allowed` | | `/data/{index}/attributes/bikes_allowed` | descending | `-bikes_allowed` | | `/data/{index}/attributes/block_id` | ascending | `block_id` | | `/data/{index}/attributes/block_id` | descending | `-block_id` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/headsign` | ascending | `headsign` | | `/data/{index}/attributes/headsign` | descending | `-headsign` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/wheelchair_accessible` | ascending | `wheelchair_accessible` | | `/data/{index}/attributes/wheelchair_accessible` | descending | `-wheelchair_accessible` |  
        :param str fields_trip: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |  
        :param date filter_date: Filter by trips on a particular date The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD.
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route_pattern: Filter by route pattern IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_id: Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_name: Filter by multiple names. **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Trips, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_offset', 'page_limit', 'sort', 'fields_trip', 'include', 'filter_date', 'filter_direction_id', 'filter_route', 'filter_route_pattern', 'filter_id', 'filter_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_trip_controller_index" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page_offset' in local_var_params and local_var_params['page_offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_offset` when calling `api_web_trip_controller_index`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_limit' in local_var_params and local_var_params['page_limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_limit` when calling `api_web_trip_controller_index`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_offset' in local_var_params and local_var_params['page_offset'] is not None:  # noqa: E501
            query_params.append(('page[offset]', local_var_params['page_offset']))  # noqa: E501
        if 'page_limit' in local_var_params and local_var_params['page_limit'] is not None:  # noqa: E501
            query_params.append(('page[limit]', local_var_params['page_limit']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'fields_trip' in local_var_params and local_var_params['fields_trip'] is not None:  # noqa: E501
            query_params.append(('fields[trip]', local_var_params['fields_trip']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
        if 'filter_date' in local_var_params and local_var_params['filter_date'] is not None:  # noqa: E501
            query_params.append(('filter[date]', local_var_params['filter_date']))  # noqa: E501
        if 'filter_direction_id' in local_var_params and local_var_params['filter_direction_id'] is not None:  # noqa: E501
            query_params.append(('filter[direction_id]', local_var_params['filter_direction_id']))  # noqa: E501
        if 'filter_route' in local_var_params and local_var_params['filter_route'] is not None:  # noqa: E501
            query_params.append(('filter[route]', local_var_params['filter_route']))  # noqa: E501
        if 'filter_route_pattern' in local_var_params and local_var_params['filter_route_pattern'] is not None:  # noqa: E501
            query_params.append(('filter[route_pattern]', local_var_params['filter_route_pattern']))  # noqa: E501
        if 'filter_id' in local_var_params and local_var_params['filter_id'] is not None:  # noqa: E501
            query_params.append(('filter[id]', local_var_params['filter_id']))  # noqa: E501
        if 'filter_name' in local_var_params and local_var_params['filter_name'] is not None:  # noqa: E501
            query_params.append(('filter[name]', local_var_params['filter_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key_in_header', 'api_key_in_query']  # noqa: E501

        return self.api_client.call_api(
            '/trips', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Trips',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_web_trip_controller_show(self, id, **kwargs):  # noqa: E501
        """api_web_trip_controller_show  # noqa: E501

        Single trip - the journey of a particular vehicle through a set of stops  ## Accessibility  Wheelchair accessibility (`/data/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_trip_controller_show(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Unique identifier for a trip (required)
        :param str fields_trip: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |  
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Trip
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_web_trip_controller_show_with_http_info(id, **kwargs)  # noqa: E501

    def api_web_trip_controller_show_with_http_info(self, id, **kwargs):  # noqa: E501
        """api_web_trip_controller_show  # noqa: E501

        Single trip - the journey of a particular vehicle through a set of stops  ## Accessibility  Wheelchair accessibility (`/data/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_trip_controller_show_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Unique identifier for a trip (required)
        :param str fields_trip: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |  
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Trip, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'fields_trip', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_trip_controller_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `api_web_trip_controller_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'fields_trip' in local_var_params and local_var_params['fields_trip'] is not None:  # noqa: E501
            query_params.append(('fields[trip]', local_var_params['fields_trip']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key_in_header', 'api_key_in_query']  # noqa: E501

        return self.api_client.call_api(
            '/trips/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Trip',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)