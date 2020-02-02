# openapi_client.TripApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_trip_controller_index**](TripApi.md#api_web_trip_controller_index) | **GET** /trips | 
[**api_web_trip_controller_show**](TripApi.md#api_web_trip_controller_show) | **GET** /trips/{id} | 


# **api_web_trip_controller_index**
> Trips api_web_trip_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_trip=fields_trip, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_route=filter_route, filter_route_pattern=filter_route_pattern, filter_id=filter_id, filter_name=filter_name)



**NOTE:** A id, route, route_pattern, or name filter **MUST** be present for any trips to be returned.  List of trips, the journies of a particular vehicle through a set of stops on a primary `route` and zero or more alternative `route`s that can be filtered on.  ## Accessibility  Wheelchair accessibility (`/data/{index}/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/{index}/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |   

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
    api_instance = openapi_client.TripApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bikes_allowed` | ascending | `bikes_allowed` | | `/data/{index}/attributes/bikes_allowed` | descending | `-bikes_allowed` | | `/data/{index}/attributes/block_id` | ascending | `block_id` | | `/data/{index}/attributes/block_id` | descending | `-block_id` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/headsign` | ascending | `headsign` | | `/data/{index}/attributes/headsign` | descending | `-headsign` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/wheelchair_accessible` | ascending | `wheelchair_accessible` | | `/data/{index}/attributes/wheelchair_accessible` | descending | `-wheelchair_accessible` |   (optional)
fields_trip = 'fields_trip_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |   (optional)
filter_date = '2013-10-20' # date | Filter by trips on a particular date The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route_pattern = 'Red-1-0,Red-1-1' # str | Filter by route pattern IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_id = '1,2' # str | Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_name = '300,302' # str | Filter by multiple names. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_trip_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_trip=fields_trip, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_route=filter_route, filter_route_pattern=filter_route_pattern, filter_id=filter_id, filter_name=filter_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TripApi->api_web_trip_controller_index: %s\n" % e)
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
    api_instance = openapi_client.TripApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bikes_allowed` | ascending | `bikes_allowed` | | `/data/{index}/attributes/bikes_allowed` | descending | `-bikes_allowed` | | `/data/{index}/attributes/block_id` | ascending | `block_id` | | `/data/{index}/attributes/block_id` | descending | `-block_id` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/headsign` | ascending | `headsign` | | `/data/{index}/attributes/headsign` | descending | `-headsign` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/wheelchair_accessible` | ascending | `wheelchair_accessible` | | `/data/{index}/attributes/wheelchair_accessible` | descending | `-wheelchair_accessible` |   (optional)
fields_trip = 'fields_trip_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |   (optional)
filter_date = '2013-10-20' # date | Filter by trips on a particular date The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route_pattern = 'Red-1-0,Red-1-1' # str | Filter by route pattern IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_id = '1,2' # str | Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_name = '300,302' # str | Filter by multiple names. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_trip_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_trip=fields_trip, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_route=filter_route, filter_route_pattern=filter_route_pattern, filter_id=filter_id, filter_name=filter_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TripApi->api_web_trip_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/bikes_allowed&#x60; | ascending | &#x60;bikes_allowed&#x60; | | &#x60;/data/{index}/attributes/bikes_allowed&#x60; | descending | &#x60;-bikes_allowed&#x60; | | &#x60;/data/{index}/attributes/block_id&#x60; | ascending | &#x60;block_id&#x60; | | &#x60;/data/{index}/attributes/block_id&#x60; | descending | &#x60;-block_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/headsign&#x60; | ascending | &#x60;headsign&#x60; | | &#x60;/data/{index}/attributes/headsign&#x60; | descending | &#x60;-headsign&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | ascending | &#x60;name&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | descending | &#x60;-name&#x60; | | &#x60;/data/{index}/attributes/wheelchair_accessible&#x60; | ascending | &#x60;wheelchair_accessible&#x60; | | &#x60;/data/{index}/attributes/wheelchair_accessible&#x60; | descending | &#x60;-wheelchair_accessible&#x60; |   | [optional] 
 **fields_trip** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;vehicle&#x60; * &#x60;service&#x60; * &#x60;shape&#x60; * &#x60;predictions&#x60; * &#x60;route_pattern&#x60; * &#x60;stops&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | &#x60;route&#x60;         | The *primary* route for the trip. | | &#x60;vehicle&#x60;       | The vehicle on this trip. | | &#x60;service&#x60;       | The service controlling when this trip is active. | | &#x60;shape&#x60;         | The shape of the trip. | | &#x60;route_pattern&#x60; | The route pattern for the trip. | | &#x60;predictions&#x60;   | Predictions of when the &#x60;vehicle&#x60; on this &#x60;trip&#x60; will arrive at or depart from each stop on the route(s) on the &#x60;trip&#x60;. | | &#x60;stops&#x60;         | The stops this trip goes through. |   | [optional] 
 **filter_date** | **date**| Filter by trips on a particular date The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_route_pattern** | **str**| Filter by route pattern IDs **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_id** | **str**| Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_name** | **str**| Filter by multiple names. **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**Trips**](Trips.md)

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

# **api_web_trip_controller_show**
> Trip api_web_trip_controller_show(id, fields_trip=fields_trip, include=include)



Single trip - the journey of a particular vehicle through a set of stops  ## Accessibility  Wheelchair accessibility (`/data/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |   

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
    api_instance = openapi_client.TripApi(api_client)
    id = 'id_example' # str | Unique identifier for a trip
fields_trip = 'fields_trip_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |   (optional)

    try:
        api_response = api_instance.api_web_trip_controller_show(id, fields_trip=fields_trip, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TripApi->api_web_trip_controller_show: %s\n" % e)
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
    api_instance = openapi_client.TripApi(api_client)
    id = 'id_example' # str | Unique identifier for a trip
fields_trip = 'fields_trip_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `vehicle` * `service` * `shape` * `predictions` * `route_pattern` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | `route`         | The *primary* route for the trip. | | `vehicle`       | The vehicle on this trip. | | `service`       | The service controlling when this trip is active. | | `shape`         | The shape of the trip. | | `route_pattern` | The route pattern for the trip. | | `predictions`   | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. | | `stops`         | The stops this trip goes through. |   (optional)

    try:
        api_response = api_instance.api_web_trip_controller_show(id, fields_trip=fields_trip, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TripApi->api_web_trip_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a trip | 
 **fields_trip** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;vehicle&#x60; * &#x60;service&#x60; * &#x60;shape&#x60; * &#x60;predictions&#x60; * &#x60;route_pattern&#x60; * &#x60;stops&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include         | Description | |-----------------|-------------| | &#x60;route&#x60;         | The *primary* route for the trip. | | &#x60;vehicle&#x60;       | The vehicle on this trip. | | &#x60;service&#x60;       | The service controlling when this trip is active. | | &#x60;shape&#x60;         | The shape of the trip. | | &#x60;route_pattern&#x60; | The route pattern for the trip. | | &#x60;predictions&#x60;   | Predictions of when the &#x60;vehicle&#x60; on this &#x60;trip&#x60; will arrive at or depart from each stop on the route(s) on the &#x60;trip&#x60;. | | &#x60;stops&#x60;         | The stops this trip goes through. |   | [optional] 

### Return type

[**Trip**](Trip.md)

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

