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


class ShapeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_web_shape_controller_index(self, filter_route, **kwargs):  # noqa: E501
        """api_web_shape_controller_index  # noqa: E501

        **NOTE:** `filter[route]` **MUST** be given for any shapes to be returned.  List of shapes.  ## Vertices  ### World  `/data/{index}/attributes/polyline` is in [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which encodes the latitude and longitude of a sequence of points in the shape.  ### Stops  If instead of getting the latitude and longitude directly, you want to show the stops in this shape use `/data/{index}/relationships/stops` to get the all the stop IDs or `include=stops` to include them in the response.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_shape_controller_index(filter_route, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (required)
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/polyline` | ascending | `polyline` | | `/data/{index}/attributes/polyline` | descending | `-polyline` | | `/data/{index}/attributes/priority` | ascending | `priority` | | `/data/{index}/attributes/priority` | descending | `-priority` |  
        :param str fields_shape: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Shapes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_web_shape_controller_index_with_http_info(filter_route, **kwargs)  # noqa: E501

    def api_web_shape_controller_index_with_http_info(self, filter_route, **kwargs):  # noqa: E501
        """api_web_shape_controller_index  # noqa: E501

        **NOTE:** `filter[route]` **MUST** be given for any shapes to be returned.  List of shapes.  ## Vertices  ### World  `/data/{index}/attributes/polyline` is in [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which encodes the latitude and longitude of a sequence of points in the shape.  ### Stops  If instead of getting the latitude and longitude directly, you want to show the stops in this shape use `/data/{index}/relationships/stops` to get the all the stop IDs or `include=stops` to include them in the response.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_shape_controller_index_with_http_info(filter_route, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str filter_route: Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (required)
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/polyline` | ascending | `polyline` | | `/data/{index}/attributes/polyline` | descending | `-polyline` | | `/data/{index}/attributes/priority` | ascending | `priority` | | `/data/{index}/attributes/priority` | descending | `-priority` |  
        :param str fields_shape: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Shapes, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['filter_route', 'page_offset', 'page_limit', 'sort', 'fields_shape', 'include', 'filter_direction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_shape_controller_index" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'filter_route' is set
        if self.api_client.client_side_validation and ('filter_route' not in local_var_params or  # noqa: E501
                                                        local_var_params['filter_route'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `filter_route` when calling `api_web_shape_controller_index`")  # noqa: E501

        if self.api_client.client_side_validation and 'page_offset' in local_var_params and local_var_params['page_offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_offset` when calling `api_web_shape_controller_index`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_limit' in local_var_params and local_var_params['page_limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_limit` when calling `api_web_shape_controller_index`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_offset' in local_var_params and local_var_params['page_offset'] is not None:  # noqa: E501
            query_params.append(('page[offset]', local_var_params['page_offset']))  # noqa: E501
        if 'page_limit' in local_var_params and local_var_params['page_limit'] is not None:  # noqa: E501
            query_params.append(('page[limit]', local_var_params['page_limit']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'fields_shape' in local_var_params and local_var_params['fields_shape'] is not None:  # noqa: E501
            query_params.append(('fields[shape]', local_var_params['fields_shape']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
        if 'filter_route' in local_var_params and local_var_params['filter_route'] is not None:  # noqa: E501
            query_params.append(('filter[route]', local_var_params['filter_route']))  # noqa: E501
        if 'filter_direction_id' in local_var_params and local_var_params['filter_direction_id'] is not None:  # noqa: E501
            query_params.append(('filter[direction_id]', local_var_params['filter_direction_id']))  # noqa: E501

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
            '/shapes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shapes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_web_shape_controller_show(self, id, **kwargs):  # noqa: E501
        """api_web_shape_controller_show  # noqa: E501

        Detail of a particular shape.  ## Vertices  ### World  `/data/attributes/polyline` is in [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which encodes the latitude and longitude of a sequence of points in the shape.  ### Stops  If instead of getting the latitude and longitude directly, you want to show the stops in this shape use `/data/relationships/stops` to get the all the stop IDs or `include=stops` to include them in the response.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_shape_controller_show(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Unique identifier for shape (required)
        :param str fields_shape: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Shape
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_web_shape_controller_show_with_http_info(id, **kwargs)  # noqa: E501

    def api_web_shape_controller_show_with_http_info(self, id, **kwargs):  # noqa: E501
        """api_web_shape_controller_show  # noqa: E501

        Detail of a particular shape.  ## Vertices  ### World  `/data/attributes/polyline` is in [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which encodes the latitude and longitude of a sequence of points in the shape.  ### Stops  If instead of getting the latitude and longitude directly, you want to show the stops in this shape use `/data/relationships/stops` to get the all the stop IDs or `include=stops` to include them in the response.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_web_shape_controller_show_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Unique identifier for shape (required)
        :param str fields_shape: Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example. 
        :param str include: Relationships to include.  * `route` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)   
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Shape, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'fields_shape', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_shape_controller_show" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `api_web_shape_controller_show`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'fields_shape' in local_var_params and local_var_params['fields_shape'] is not None:  # noqa: E501
            query_params.append(('fields[shape]', local_var_params['fields_shape']))  # noqa: E501
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
            '/shapes/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shape',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)