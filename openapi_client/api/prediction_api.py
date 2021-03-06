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


class PredictionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_web_prediction_controller_index(self, **kwargs):  # noqa: E501
        """api_web_prediction_controller_index  # noqa: E501

        **NOTE:** A filter **MUST** be present for any predictions to be returned.  List of predictions for trips.  To get the scheduled times instead of the predictions, use `/schedules`.  The predicted arrival time (`//data/{index}/attributes/arrival_time`) and departure time (`/data/{index}/attributes/departure_time`) to/from a stop (`/data/{index}/relationships/stop/data/id`) at a given sequence (`/data/{index}/attriutes/stop_sequence`) along a trip (`/data/{index}/relationships/trip/data/id`) going a direction (`/data/{index}/attributes/direction_id`) along a route (`/data/{index}/relationships/route/data/id`).  See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `TripDescriptor`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-tripdescriptor) See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `StopTimeUpdate`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-stoptimeupdate)   ## When a vehicle is predicted to be at a stop  `/predictions?filter[stop]=STOP_ID`  ## The predicted schedule for one route  `/predictions?filter[route]=ROUTE_ID`  ## The predicted schedule for a whole trip  `/predictions?filter[trip]=TRIP_ID`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_prediction_controller_index(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key.  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/schedule_relationship` | ascending | `schedule_relationship` | | `/data/{index}/attributes/schedule_relationship` | descending | `-schedule_relationship` | | `/data/{index}/attributes/status` | ascending | `status` | | `/data/{index}/attributes/status` | descending | `-status` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` |  | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | ascending | `time` | | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | descending | `-time` |  
        :param str fields_prediction: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `schedule` * `stop` * `route` * `trip` * `vehicle` * `alerts`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  Here is an example: `https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-sstat&filter%5Bdirection_id%5D=0&include=stop` returns predictions from South Station with direction_id=0, below is a truncated response with only relevant fields displayed: ```   {     \"data\": [       {         \"id\": \"prediction-CR-Weekday-Fall-18-743-South Station-02-1\",         \"relationships\": {           \"stop\": {             \"data\": {               \"id\": \"South Station-02\",               \"type\": \"stop\"             }           },         },         \"type\": \"prediction\"       }     ],     \"included\": [       {         \"attributes\": {           \"platform_code\": \"2\",         },         \"id\": \"South Station-02\",         \"type\": \"stop\"       }     ],   } ``` Note the stop relationship; use it to cross-reference  stop-id with the included stops to retrieve the platform_code for the given prediction.  
        :param str filter_latitude:  Latitude/Longitude must be both present or both absent.
        :param str filter_longitude:  Latitude/Longitude must be both present or both absent.
        :param date filter_radius:  Radius accepts a floating point number, and the default is 0.01.  For example, if you query for: latitude: 42,  longitude: -71,  radius: 0.05 then you will filter between latitudes 41.95 and 42.05, and longitudes -70.95 and -71.05.
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param str filter_route_type: Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list. 
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_trip: Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route_pattern: Filter by `/included/{index}/relationships/route_pattern/data/id` of a trip. Multiple `route_pattern_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Predictions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_web_prediction_controller_index_with_http_info(**kwargs)  # noqa: E501

    def api_web_prediction_controller_index_with_http_info(self, **kwargs):  # noqa: E501
        """api_web_prediction_controller_index  # noqa: E501

        **NOTE:** A filter **MUST** be present for any predictions to be returned.  List of predictions for trips.  To get the scheduled times instead of the predictions, use `/schedules`.  The predicted arrival time (`//data/{index}/attributes/arrival_time`) and departure time (`/data/{index}/attributes/departure_time`) to/from a stop (`/data/{index}/relationships/stop/data/id`) at a given sequence (`/data/{index}/attriutes/stop_sequence`) along a trip (`/data/{index}/relationships/trip/data/id`) going a direction (`/data/{index}/attributes/direction_id`) along a route (`/data/{index}/relationships/route/data/id`).  See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `TripDescriptor`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-tripdescriptor) See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `StopTimeUpdate`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-stoptimeupdate)   ## When a vehicle is predicted to be at a stop  `/predictions?filter[stop]=STOP_ID`  ## The predicted schedule for one route  `/predictions?filter[route]=ROUTE_ID`  ## The predicted schedule for a whole trip  `/predictions?filter[trip]=TRIP_ID`    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_prediction_controller_index_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key.  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/schedule_relationship` | ascending | `schedule_relationship` | | `/data/{index}/attributes/schedule_relationship` | descending | `-schedule_relationship` | | `/data/{index}/attributes/status` | ascending | `status` | | `/data/{index}/attributes/status` | descending | `-status` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` |  | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | ascending | `time` | | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | descending | `-time` |  
        :param str fields_prediction: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `schedule` * `stop` * `route` * `trip` * `vehicle` * `alerts`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  Here is an example: `https://api-v3.mbta.com/predictions?filter%5Bstop%5D=place-sstat&filter%5Bdirection_id%5D=0&include=stop` returns predictions from South Station with direction_id=0, below is a truncated response with only relevant fields displayed: ```   {     \"data\": [       {         \"id\": \"prediction-CR-Weekday-Fall-18-743-South Station-02-1\",         \"relationships\": {           \"stop\": {             \"data\": {               \"id\": \"South Station-02\",               \"type\": \"stop\"             }           },         },         \"type\": \"prediction\"       }     ],     \"included\": [       {         \"attributes\": {           \"platform_code\": \"2\",         },         \"id\": \"South Station-02\",         \"type\": \"stop\"       }     ],   } ``` Note the stop relationship; use it to cross-reference  stop-id with the included stops to retrieve the platform_code for the given prediction.  
        :param str filter_latitude:  Latitude/Longitude must be both present or both absent.
        :param str filter_longitude:  Latitude/Longitude must be both present or both absent.
        :param date filter_radius:  Radius accepts a floating point number, and the default is 0.01.  For example, if you query for: latitude: 42,  longitude: -71,  radius: 0.05 then you will filter between latitudes 41.95 and 42.05, and longitudes -70.95 and -71.05.
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param str filter_route_type: Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list. 
        :param str filter_stop: Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_trip: Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route_pattern: Filter by `/included/{index}/relationships/route_pattern/data/id` of a trip. Multiple `route_pattern_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Predictions, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_offset', 'page_limit', 'sort', 'fields_prediction', 'include', 'filter_latitude', 'filter_longitude', 'filter_radius', 'filter_direction_id', 'filter_route_type', 'filter_stop', 'filter_route', 'filter_trip', 'filter_route_pattern']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_prediction_controller_index" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'page_offset' in local_var_params and local_var_params['page_offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_offset` when calling `api_web_prediction_controller_index`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_limit' in local_var_params and local_var_params['page_limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_limit` when calling `api_web_prediction_controller_index`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_offset' in local_var_params and local_var_params['page_offset'] is not None:  # noqa: E501
            query_params.append(('page[offset]', local_var_params['page_offset']))  # noqa: E501
        if 'page_limit' in local_var_params and local_var_params['page_limit'] is not None:  # noqa: E501
            query_params.append(('page[limit]', local_var_params['page_limit']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'fields_prediction' in local_var_params and local_var_params['fields_prediction'] is not None:  # noqa: E501
            query_params.append(('fields[prediction]', local_var_params['fields_prediction']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
        if 'filter_latitude' in local_var_params and local_var_params['filter_latitude'] is not None:  # noqa: E501
            query_params.append(('filter[latitude]', local_var_params['filter_latitude']))  # noqa: E501
        if 'filter_longitude' in local_var_params and local_var_params['filter_longitude'] is not None:  # noqa: E501
            query_params.append(('filter[longitude]', local_var_params['filter_longitude']))  # noqa: E501
        if 'filter_radius' in local_var_params and local_var_params['filter_radius'] is not None:  # noqa: E501
            query_params.append(('filter[radius]', local_var_params['filter_radius']))  # noqa: E501
        if 'filter_direction_id' in local_var_params and local_var_params['filter_direction_id'] is not None:  # noqa: E501
            query_params.append(('filter[direction_id]', local_var_params['filter_direction_id']))  # noqa: E501
        if 'filter_route_type' in local_var_params and local_var_params['filter_route_type'] is not None:  # noqa: E501
            query_params.append(('filter[route_type]', local_var_params['filter_route_type']))  # noqa: E501
        if 'filter_stop' in local_var_params and local_var_params['filter_stop'] is not None:  # noqa: E501
            query_params.append(('filter[stop]', local_var_params['filter_stop']))  # noqa: E501
        if 'filter_route' in local_var_params and local_var_params['filter_route'] is not None:  # noqa: E501
            query_params.append(('filter[route]', local_var_params['filter_route']))  # noqa: E501
        if 'filter_trip' in local_var_params and local_var_params['filter_trip'] is not None:  # noqa: E501
            query_params.append(('filter[trip]', local_var_params['filter_trip']))  # noqa: E501
        if 'filter_route_pattern' in local_var_params and local_var_params['filter_route_pattern'] is not None:  # noqa: E501
            query_params.append(('filter[route_pattern]', local_var_params['filter_route_pattern']))  # noqa: E501

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
            '/predictions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Predictions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
