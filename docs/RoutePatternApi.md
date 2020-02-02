# openapi_client.RoutePatternApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_route_pattern_controller_index**](RoutePatternApi.md#api_web_route_pattern_controller_index) | **GET** /route_patterns | 
[**api_web_route_pattern_controller_show**](RoutePatternApi.md#api_web_route_pattern_controller_show) | **GET** /route_patterns/{id} | 


# **api_web_route_pattern_controller_index**
> RoutePattern api_web_route_pattern_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, include=include, filter_id=filter_id, filter_route=filter_route, filter_direction_id=filter_direction_id, filter_stop=filter_stop)



List of route patterns.  Route patterns are used to describe the subsets of a route, representing different possible patterns of where trips may serve. For example, a bus route may have multiple branches, and each branch may be modeled as a separate route pattern per direction. Hierarchically, the route pattern level may be considered to be larger than the trip level and smaller than the route level.  For most MBTA modes, a route pattern will typically represent a unique set of stops that may be served on a route-trip combination. Seasonal schedule changes may result in trips within a route pattern having different routings. In simple changes, such a single bus stop removed or added between one schedule rating and the next (for example, between the Summer and Fall schedules), trips will be maintained on the same route_pattern_id. If the changes are significant, a new route_pattern_id may be introduced.  For Commuter Rail, express or skip-stop trips use the same route pattern as local trips. Some branches do have multiple route patterns when the train takes a different path. For example, `CR-Providence` has two route patterns per direction, one for the Wickford Junction branch and the other for the Stoughton branch.  

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
    api_instance = openapi_client.RoutePatternApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/sort_order` | ascending | `sort_order` | | `/data/{index}/attributes/sort_order` | descending | `-sort_order` | | `/data/{index}/attributes/time_desc` | ascending | `time_desc` | | `/data/{index}/attributes/time_desc` | descending | `-time_desc` | | `/data/{index}/attributes/typicality` | ascending | `typicality` | | `/data/{index}/attributes/typicality` | descending | `-typicality` |   (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `representative_trip`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description | |-|-| | `route` | The route that this pattern belongs to. | | `representative_trip` | A trip that can be considered a canonical trip for the route pattern. This trip can be used to deduce a pattern's canonical set of stops and shape. |   (optional)
filter_id = 'Red-1-0,Red-1-1' # str | Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_route_pattern_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, include=include, filter_id=filter_id, filter_route=filter_route, filter_direction_id=filter_direction_id, filter_stop=filter_stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutePatternApi->api_web_route_pattern_controller_index: %s\n" % e)
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
    api_instance = openapi_client.RoutePatternApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/sort_order` | ascending | `sort_order` | | `/data/{index}/attributes/sort_order` | descending | `-sort_order` | | `/data/{index}/attributes/time_desc` | ascending | `time_desc` | | `/data/{index}/attributes/time_desc` | descending | `-time_desc` | | `/data/{index}/attributes/typicality` | ascending | `typicality` | | `/data/{index}/attributes/typicality` | descending | `-typicality` |   (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `representative_trip`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description | |-|-| | `route` | The route that this pattern belongs to. | | `representative_trip` | A trip that can be considered a canonical trip for the route pattern. This trip can be used to deduce a pattern's canonical set of stops and shape. |   (optional)
filter_id = 'Red-1-0,Red-1-1' # str | Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_route_pattern_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, include=include, filter_id=filter_id, filter_route=filter_route, filter_direction_id=filter_direction_id, filter_stop=filter_stop)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutePatternApi->api_web_route_pattern_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | ascending | &#x60;name&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | descending | &#x60;-name&#x60; | | &#x60;/data/{index}/attributes/sort_order&#x60; | ascending | &#x60;sort_order&#x60; | | &#x60;/data/{index}/attributes/sort_order&#x60; | descending | &#x60;-sort_order&#x60; | | &#x60;/data/{index}/attributes/time_desc&#x60; | ascending | &#x60;time_desc&#x60; | | &#x60;/data/{index}/attributes/time_desc&#x60; | descending | &#x60;-time_desc&#x60; | | &#x60;/data/{index}/attributes/typicality&#x60; | ascending | &#x60;typicality&#x60; | | &#x60;/data/{index}/attributes/typicality&#x60; | descending | &#x60;-typicality&#x60; |   | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;representative_trip&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description | |-|-| | &#x60;route&#x60; | The route that this pattern belongs to. | | &#x60;representative_trip&#x60; | A trip that can be considered a canonical trip for the route pattern. This trip can be used to deduce a pattern&#39;s canonical set of stops and shape. |   | [optional] 
 **filter_id** | **str**| Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_stop** | **str**| Filter by &#x60;/data/{index}/relationships/stop/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/stop/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**RoutePattern**](RoutePattern.md)

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

# **api_web_route_pattern_controller_show**
> RoutePattern api_web_route_pattern_controller_show(id, include=include)



Show a particular route_pattern by the route's id.  Route patterns are used to describe the subsets of a route, representing different possible patterns of where trips may serve. For example, a bus route may have multiple branches, and each branch may be modeled as a separate route pattern per direction. Hierarchically, the route pattern level may be considered to be larger than the trip level and smaller than the route level.  For most MBTA modes, a route pattern will typically represent a unique set of stops that may be served on a route-trip combination. Seasonal schedule changes may result in trips within a route pattern having different routings. In simple changes, such a single bus stop removed or added between one schedule rating and the next (for example, between the Summer and Fall schedules), trips will be maintained on the same route_pattern_id. If the changes are significant, a new route_pattern_id may be introduced.  For Commuter Rail, express or skip-stop trips use the same route pattern as local trips. Some branches do have multiple route patterns when the train takes a different path. For example, `CR-Providence` has two route patterns per direction, one for the Wickford Junction branch and the other for the Stoughton branch.  

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
    api_instance = openapi_client.RoutePatternApi(api_client)
    id = 'id_example' # str | Unique identifier for route_pattern
include = 'include_example' # str | Relationships to include.  * `route` * `representative_trip`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description | |-|-| | `route` | The route that this pattern belongs to. | | `representative_trip` | A trip that can be considered a canonical trip for the route pattern. This trip can be used to deduce a pattern's canonical set of stops and shape. |   (optional)

    try:
        api_response = api_instance.api_web_route_pattern_controller_show(id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutePatternApi->api_web_route_pattern_controller_show: %s\n" % e)
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
    api_instance = openapi_client.RoutePatternApi(api_client)
    id = 'id_example' # str | Unique identifier for route_pattern
include = 'include_example' # str | Relationships to include.  * `route` * `representative_trip`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description | |-|-| | `route` | The route that this pattern belongs to. | | `representative_trip` | A trip that can be considered a canonical trip for the route pattern. This trip can be used to deduce a pattern's canonical set of stops and shape. |   (optional)

    try:
        api_response = api_instance.api_web_route_pattern_controller_show(id, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutePatternApi->api_web_route_pattern_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for route_pattern | 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;representative_trip&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description | |-|-| | &#x60;route&#x60; | The route that this pattern belongs to. | | &#x60;representative_trip&#x60; | A trip that can be considered a canonical trip for the route pattern. This trip can be used to deduce a pattern&#39;s canonical set of stops and shape. |   | [optional] 

### Return type

[**RoutePattern**](RoutePattern.md)

### Authorization

[api_key_in_header](../README.md#api_key_in_header), [api_key_in_query](../README.md#api_key_in_query)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

