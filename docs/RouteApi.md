# openapi_client.RouteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_route_controller_index**](RouteApi.md#api_web_route_controller_index) | **GET** /routes | 
[**api_web_route_controller_show**](RouteApi.md#api_web_route_controller_show) | **GET** /routes/{id} | 


# **api_web_route_controller_index**
> Routes api_web_route_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_route=fields_route, include=include, filter_stop=filter_stop, filter_type=filter_type, filter_direction_id=filter_direction_id, filter_date=filter_date, filter_id=filter_id)



List of routes.  ## Names and Descriptions  There are 3 attributes with increasing details for naming and describing the route.  1. `/data/{index}/attributes/short_name` 2. `/data/{index}/attributes/long_name` 3. `/data/{index}/attributes/description`  ## Directions  `/data/{index}/attributes/direction_names` is the only place to convert the `direction_id` used throughout the rest of the API to human-readable names.  ## Type  `/data/{index}/attributes/type` corresponds to [GTFS `routes.txt` `route_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   

### Example

* Api Key Authentication (api_key_in_header):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_header
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_query
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RouteApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/color` | ascending | `color` | | `/data/{index}/attributes/color` | descending | `-color` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/direction_destinations` | ascending | `direction_destinations` | | `/data/{index}/attributes/direction_destinations` | descending | `-direction_destinations` | | `/data/{index}/attributes/direction_names` | ascending | `direction_names` | | `/data/{index}/attributes/direction_names` | descending | `-direction_names` | | `/data/{index}/attributes/fare_class` | ascending | `fare_class` | | `/data/{index}/attributes/fare_class` | descending | `-fare_class` | | `/data/{index}/attributes/long_name` | ascending | `long_name` | | `/data/{index}/attributes/long_name` | descending | `-long_name` | | `/data/{index}/attributes/short_name` | ascending | `short_name` | | `/data/{index}/attributes/short_name` | descending | `-short_name` | | `/data/{index}/attributes/sort_order` | ascending | `sort_order` | | `/data/{index}/attributes/sort_order` | descending | `-sort_order` | | `/data/{index}/attributes/text_color` | ascending | `text_color` | | `/data/{index}/attributes/text_color` | descending | `-text_color` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |   (optional)
fields_route = 'fields_route_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop` * `line` * `route_patterns`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  include=stop only works when `filter[stop]` is also used  (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Must filter by stop in order to include stop with response (optional)
filter_type = '0' # str | | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.   When combined with stop_id, filters by routes which stop at that stop when traveling in a particular direction  (optional)
filter_date = '2013-10-20' # date | Filter by date that route is active The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_id = '1,2' # str | Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_route_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_route=fields_route, include=include, filter_stop=filter_stop, filter_type=filter_type, filter_direction_id=filter_direction_id, filter_date=filter_date, filter_id=filter_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RouteApi->api_web_route_controller_index: %s\n" % e)
```

* Api Key Authentication (api_key_in_query):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_header
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_query
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RouteApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/color` | ascending | `color` | | `/data/{index}/attributes/color` | descending | `-color` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/direction_destinations` | ascending | `direction_destinations` | | `/data/{index}/attributes/direction_destinations` | descending | `-direction_destinations` | | `/data/{index}/attributes/direction_names` | ascending | `direction_names` | | `/data/{index}/attributes/direction_names` | descending | `-direction_names` | | `/data/{index}/attributes/fare_class` | ascending | `fare_class` | | `/data/{index}/attributes/fare_class` | descending | `-fare_class` | | `/data/{index}/attributes/long_name` | ascending | `long_name` | | `/data/{index}/attributes/long_name` | descending | `-long_name` | | `/data/{index}/attributes/short_name` | ascending | `short_name` | | `/data/{index}/attributes/short_name` | descending | `-short_name` | | `/data/{index}/attributes/sort_order` | ascending | `sort_order` | | `/data/{index}/attributes/sort_order` | descending | `-sort_order` | | `/data/{index}/attributes/text_color` | ascending | `text_color` | | `/data/{index}/attributes/text_color` | descending | `-text_color` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |   (optional)
fields_route = 'fields_route_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop` * `line` * `route_patterns`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  include=stop only works when `filter[stop]` is also used  (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Must filter by stop in order to include stop with response (optional)
filter_type = '0' # str | | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.   When combined with stop_id, filters by routes which stop at that stop when traveling in a particular direction  (optional)
filter_date = '2013-10-20' # date | Filter by date that route is active The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_id = '1,2' # str | Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_route_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_route=fields_route, include=include, filter_stop=filter_stop, filter_type=filter_type, filter_direction_id=filter_direction_id, filter_date=filter_date, filter_id=filter_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RouteApi->api_web_route_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/color&#x60; | ascending | &#x60;color&#x60; | | &#x60;/data/{index}/attributes/color&#x60; | descending | &#x60;-color&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | ascending | &#x60;description&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | descending | &#x60;-description&#x60; | | &#x60;/data/{index}/attributes/direction_destinations&#x60; | ascending | &#x60;direction_destinations&#x60; | | &#x60;/data/{index}/attributes/direction_destinations&#x60; | descending | &#x60;-direction_destinations&#x60; | | &#x60;/data/{index}/attributes/direction_names&#x60; | ascending | &#x60;direction_names&#x60; | | &#x60;/data/{index}/attributes/direction_names&#x60; | descending | &#x60;-direction_names&#x60; | | &#x60;/data/{index}/attributes/fare_class&#x60; | ascending | &#x60;fare_class&#x60; | | &#x60;/data/{index}/attributes/fare_class&#x60; | descending | &#x60;-fare_class&#x60; | | &#x60;/data/{index}/attributes/long_name&#x60; | ascending | &#x60;long_name&#x60; | | &#x60;/data/{index}/attributes/long_name&#x60; | descending | &#x60;-long_name&#x60; | | &#x60;/data/{index}/attributes/short_name&#x60; | ascending | &#x60;short_name&#x60; | | &#x60;/data/{index}/attributes/short_name&#x60; | descending | &#x60;-short_name&#x60; | | &#x60;/data/{index}/attributes/sort_order&#x60; | ascending | &#x60;sort_order&#x60; | | &#x60;/data/{index}/attributes/sort_order&#x60; | descending | &#x60;-sort_order&#x60; | | &#x60;/data/{index}/attributes/text_color&#x60; | ascending | &#x60;text_color&#x60; | | &#x60;/data/{index}/attributes/text_color&#x60; | descending | &#x60;-text_color&#x60; | | &#x60;/data/{index}/attributes/type&#x60; | ascending | &#x60;type&#x60; | | &#x60;/data/{index}/attributes/type&#x60; | descending | &#x60;-type&#x60; |   | [optional] 
 **fields_route** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;stop&#x60; * &#x60;line&#x60; * &#x60;route_patterns&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  include&#x3D;stop only works when &#x60;filter[stop]&#x60; is also used  | [optional] 
 **filter_stop** | **str**| Filter by &#x60;/data/{index}/relationships/stop/data/id&#x60;. Must filter by stop in order to include stop with response | [optional] 
 **filter_type** | **str**| | Value | Name          | Example    | |-------|---------------|------------| | &#x60;0&#x60;   | Light Rail    | Green Line | | &#x60;1&#x60;   | Heavy Rail    | Red Line   | | &#x60;2&#x60;   | Commuter Rail |            | | &#x60;3&#x60;   | Bus           |            | | &#x60;4&#x60;   | Ferry         |            |   Multiple &#x60;route_type&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.   When combined with stop_id, filters by routes which stop at that stop when traveling in a particular direction  | [optional] 
 **filter_date** | **date**| Filter by date that route is active The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. | [optional] 
 **filter_id** | **str**| Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**Routes**](Routes.md)

### Authorization

[api_key_in_header](../README.md#api_key_in_header), [api_key_in_query](../README.md#api_key_in_query)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_web_route_controller_show**
> Route api_web_route_controller_show(id, fields_route=fields_route, include=include)



Show a particular route by the route's id.  ## Names and Descriptions  There are 3 attributes with increasing details for naming and describing the route.  1. `/data/attributes/short_name` 2. `/data/attributes/long_name` 3. `/data/attributes/description`  ## Directions  `/data/attributes/direction_names` is the only place to convert the `direction_id` used throughout the rest of the API to human-readable names.  ## Type  `/data/attributes/type` corresponds to [GTFS `routes.txt` `route_type`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | Value | Name          | Example    | |-------|---------------|------------| | `0`   | Light Rail    | Green Line | | `1`   | Heavy Rail    | Red Line   | | `2`   | Commuter Rail |            | | `3`   | Bus           |            | | `4`   | Ferry         |            |   

### Example

* Api Key Authentication (api_key_in_header):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_header
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_query
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RouteApi(api_client)
    id = 'id_example' # str | Unique identifier for route
fields_route = 'fields_route_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `line` * `route_patterns`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

    try:
        api_response = api_instance.api_web_route_controller_show(id, fields_route=fields_route, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RouteApi->api_web_route_controller_show: %s\n" % e)
```

* Api Key Authentication (api_key_in_query):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_header
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key_in_query
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RouteApi(api_client)
    id = 'id_example' # str | Unique identifier for route
fields_route = 'fields_route_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `line` * `route_patterns`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

    try:
        api_response = api_instance.api_web_route_controller_show(id, fields_route=fields_route, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RouteApi->api_web_route_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for route | 
 **fields_route** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;line&#x60; * &#x60;route_patterns&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

[api_key_in_header](../README.md#api_key_in_header), [api_key_in_query](../README.md#api_key_in_query)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

