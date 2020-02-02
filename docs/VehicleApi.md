# openapi_client.VehicleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_vehicle_controller_index**](VehicleApi.md#api_web_vehicle_controller_index) | **GET** /vehicles | 
[**api_web_vehicle_controller_show**](VehicleApi.md#api_web_vehicle_controller_show) | **GET** /vehicles/{id} | 


# **api_web_vehicle_controller_index**
> Vehicles api_web_vehicle_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_vehicle=fields_vehicle, include=include, filter_id=filter_id, filter_trip=filter_trip, filter_label=filter_label, filter_route=filter_route, filter_direction_id=filter_direction_id, filter_route_type=filter_route_type)



List of vehicles (buses, ferries, and trains)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/{index}/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/{index}/attributes/direction_id`.  ## Location  ### World  Use `/data/{index}/attributes/latitude` and `/data/{index}/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/{index}/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/{index}/attributes/current_status`.  ## Movement  ### World  Use `/data/{index}/attributes/speed` to get the speed of the vehicle in meters per second.  

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
    api_instance = openapi_client.VehicleApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bearing` | ascending | `bearing` | | `/data/{index}/attributes/bearing` | descending | `-bearing` | | `/data/{index}/attributes/current_status` | ascending | `current_status` | | `/data/{index}/attributes/current_status` | descending | `-current_status` | | `/data/{index}/attributes/current_stop_sequence` | ascending | `current_stop_sequence` | | `/data/{index}/attributes/current_stop_sequence` | descending | `-current_stop_sequence` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/label` | ascending | `label` | | `/data/{index}/attributes/label` | descending | `-label` | | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/speed` | ascending | `speed` | | `/data/{index}/attributes/speed` | descending | `-speed` | | `/data/{index}/attributes/updated_at` | ascending | `updated_at` | | `/data/{index}/attributes/updated_at` | descending | `-updated_at` |   (optional)
fields_vehicle = 'fields_vehicle_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   (optional)
filter_id = '1,2' # str | Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. Cannot be combined with any other filter. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. Cannot be combined with any other filter. (optional)
filter_label = 'filter_label_example' # str | Filter by label. Multiple `label` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_route = 'filter_route_example' # str | Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple `route_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.   Only used if `filter[route]` is also present.  (optional)
filter_route_type = 'filter_route_type_example' # str | Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)

    try:
        api_response = api_instance.api_web_vehicle_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_vehicle=fields_vehicle, include=include, filter_id=filter_id, filter_trip=filter_trip, filter_label=filter_label, filter_route=filter_route, filter_direction_id=filter_direction_id, filter_route_type=filter_route_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehicleApi->api_web_vehicle_controller_index: %s\n" % e)
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
    api_instance = openapi_client.VehicleApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bearing` | ascending | `bearing` | | `/data/{index}/attributes/bearing` | descending | `-bearing` | | `/data/{index}/attributes/current_status` | ascending | `current_status` | | `/data/{index}/attributes/current_status` | descending | `-current_status` | | `/data/{index}/attributes/current_stop_sequence` | ascending | `current_stop_sequence` | | `/data/{index}/attributes/current_stop_sequence` | descending | `-current_stop_sequence` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/label` | ascending | `label` | | `/data/{index}/attributes/label` | descending | `-label` | | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/speed` | ascending | `speed` | | `/data/{index}/attributes/speed` | descending | `-speed` | | `/data/{index}/attributes/updated_at` | ascending | `updated_at` | | `/data/{index}/attributes/updated_at` | descending | `-updated_at` |   (optional)
fields_vehicle = 'fields_vehicle_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   (optional)
filter_id = '1,2' # str | Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. Cannot be combined with any other filter. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. Cannot be combined with any other filter. (optional)
filter_label = 'filter_label_example' # str | Filter by label. Multiple `label` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_route = 'filter_route_example' # str | Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple `route_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.   Only used if `filter[route]` is also present.  (optional)
filter_route_type = 'filter_route_type_example' # str | Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)

    try:
        api_response = api_instance.api_web_vehicle_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_vehicle=fields_vehicle, include=include, filter_id=filter_id, filter_trip=filter_trip, filter_label=filter_label, filter_route=filter_route, filter_direction_id=filter_direction_id, filter_route_type=filter_route_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehicleApi->api_web_vehicle_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/bearing&#x60; | ascending | &#x60;bearing&#x60; | | &#x60;/data/{index}/attributes/bearing&#x60; | descending | &#x60;-bearing&#x60; | | &#x60;/data/{index}/attributes/current_status&#x60; | ascending | &#x60;current_status&#x60; | | &#x60;/data/{index}/attributes/current_status&#x60; | descending | &#x60;-current_status&#x60; | | &#x60;/data/{index}/attributes/current_stop_sequence&#x60; | ascending | &#x60;current_stop_sequence&#x60; | | &#x60;/data/{index}/attributes/current_stop_sequence&#x60; | descending | &#x60;-current_stop_sequence&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/label&#x60; | ascending | &#x60;label&#x60; | | &#x60;/data/{index}/attributes/label&#x60; | descending | &#x60;-label&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | ascending | &#x60;latitude&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | descending | &#x60;-latitude&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | ascending | &#x60;longitude&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | descending | &#x60;-longitude&#x60; | | &#x60;/data/{index}/attributes/speed&#x60; | ascending | &#x60;speed&#x60; | | &#x60;/data/{index}/attributes/speed&#x60; | descending | &#x60;-speed&#x60; | | &#x60;/data/{index}/attributes/updated_at&#x60; | ascending | &#x60;updated_at&#x60; | | &#x60;/data/{index}/attributes/updated_at&#x60; | descending | &#x60;-updated_at&#x60; |   | [optional] 
 **fields_vehicle** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;trip&#x60; * &#x60;stop&#x60; * &#x60;route&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | &#x60;trip&#x60;  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | &#x60;stop&#x60;  | The vehicle&#39;s current (when &#x60;current_status&#x60; is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | &#x60;route&#x60; | The one route that is designated for that trip, as in GTFS &#x60;trips.txt&#x60;.  A trip might also provide service on other routes, identified by the MBTA&#39;s &#x60;multi_route_trips.txt&#x60; GTFS extension. &#x60;filter[route]&#x60; does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   | [optional] 
 **filter_id** | **str**| Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. Cannot be combined with any other filter. | [optional] 
 **filter_trip** | **str**| Filter by &#x60;/data/{index}/relationships/trip/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/trip/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. Cannot be combined with any other filter. | [optional] 
 **filter_label** | **str**| Filter by label. Multiple &#x60;label&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_route** | **str**| Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple &#x60;route_id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.   Only used if &#x60;filter[route]&#x60; is also present.  | [optional] 
 **filter_route_type** | **str**| Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple &#x60;route_type&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 

### Return type

[**Vehicles**](Vehicles.md)

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

# **api_web_vehicle_controller_show**
> Vehicle api_web_vehicle_controller_show(id, fields_vehicle=fields_vehicle, include=include)



Single vehicle (bus, ferry, or train)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/attributes/direction_id`.  ## Location  ### World  Use `/data/attributes/latitude` and `/data/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/attributes/current_status`.  ## Movement  ### World  Use `/data/attributes/speed` to get the speed of the vehicle in meters per second.  

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
    api_instance = openapi_client.VehicleApi(api_client)
    id = 'id_example' # str | Unique identifier for a vehicle
fields_vehicle = 'fields_vehicle_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   (optional)

    try:
        api_response = api_instance.api_web_vehicle_controller_show(id, fields_vehicle=fields_vehicle, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehicleApi->api_web_vehicle_controller_show: %s\n" % e)
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
    api_instance = openapi_client.VehicleApi(api_client)
    id = 'id_example' # str | Unique identifier for a vehicle
fields_vehicle = 'fields_vehicle_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   (optional)

    try:
        api_response = api_instance.api_web_vehicle_controller_show(id, fields_vehicle=fields_vehicle, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VehicleApi->api_web_vehicle_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a vehicle | 
 **fields_vehicle** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;trip&#x60; * &#x60;stop&#x60; * &#x60;route&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | &#x60;trip&#x60;  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | &#x60;stop&#x60;  | The vehicle&#39;s current (when &#x60;current_status&#x60; is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | &#x60;route&#x60; | The one route that is designated for that trip, as in GTFS &#x60;trips.txt&#x60;.  A trip might also provide service on other routes, identified by the MBTA&#39;s &#x60;multi_route_trips.txt&#x60; GTFS extension. &#x60;filter[route]&#x60; does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   | [optional] 

### Return type

[**Vehicle**](Vehicle.md)

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

