# openapi_client.ScheduleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_schedule_controller_index**](ScheduleApi.md#api_web_schedule_controller_index) | **GET** /schedules | 


# **api_web_schedule_controller_index**
> Schedules api_web_schedule_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_schedule=fields_schedule, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_min_time=filter_min_time, filter_max_time=filter_max_time, filter_route=filter_route, filter_stop=filter_stop, filter_trip=filter_trip, filter_stop_sequence=filter_stop_sequence)



**NOTE:** `filter[route]`, `filter[stop]`, or `filter[trip]` **MUST** be present for any schedules to be returned.  List of schedules.  To get a realtime prediction instead of the scheduled times, use `/predictions`.  A schedule is the arrival drop off (`/data/{index}/attributes/drop_off_type`) time (`/data/{index}/attributes/arrival_time`) and departure pick up (`/data/{index}/attributes/pickup_type`) time (`/data/{index}/attributes/departure_time`) to/from a stop (`/data/{index}/relationships/stop/data/id`) at a given sequence (`/data/{index}/attributes/stop_sequence`) along a trip (`/data/{index}/relationships/trip/data/id`) going in a direction (`/data/{index}/attributes/direction_id`) on a route (`/data/{index}/relationships/route/data/id`) when the trip is following a service (`/data/{index}/relationships/service/data/id`) to determine when it is active.  See [GTFS `stop_times.txt`](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stop_timestxt) for base specification.   ## When a vehicle is scheduled to be at a stop  `/schedules?filter[stop]=STOP_ID`  ## The schedule for one route  `/schedules?filter[route]=ROUTE_ID`  ### When a route is open  Query for the `first` and `last` stops on the route.  `/schedules?filter[route]=ROUTE_ID&filter[stop_sequence]=first,last`  ## The schedule for a whole trip  `/schedule?filter[trip]=TRIP_ID`  

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
    api_instance = openapi_client.ScheduleApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key.  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/drop_off_type` | ascending | `drop_off_type` | | `/data/{index}/attributes/drop_off_type` | descending | `-drop_off_type` | | `/data/{index}/attributes/pickup_type` | ascending | `pickup_type` | | `/data/{index}/attributes/pickup_type` | descending | `-pickup_type` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` | | `/data/{index}/attributes/timepoint` | ascending | `timepoint` | | `/data/{index}/attributes/timepoint` | descending | `-timepoint` |  | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | ascending | `time` | | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | descending | `-time` |   (optional)
fields_schedule = 'fields_schedule_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop` * `trip` * `prediction` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_date = '2013-10-20' # date | Filter schedule by date that they are active. The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_min_time = 'filter_min_time_example' # str | Time before which schedule should not be returned. To filter times after midnight use more than 24 hours. For example, min_time=24:00 will return schedule information for the next calendar day, since that service is considered part of the current service day. Additionally, min_time=00:00&max_time=02:00 will not return anything. The time format is HH:MM. (optional)
filter_max_time = 'filter_max_time_example' # str | Time after which schedule should not be returned. To filter times after midnight use more than 24 hours. For example, min_time=24:00 will return schedule information for the next calendar day, since that service is considered part of the current service day. Additionally, min_time=00:00&max_time=02:00 will not return anything. The time format is HH:MM. (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_stop_sequence = 'filter_stop_sequence_example' # str | Filter by the index of the stop in the trip.  Symbolic values `first` and `last` can be used instead of numeric sequence number too.  (optional)

    try:
        api_response = api_instance.api_web_schedule_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_schedule=fields_schedule, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_min_time=filter_min_time, filter_max_time=filter_max_time, filter_route=filter_route, filter_stop=filter_stop, filter_trip=filter_trip, filter_stop_sequence=filter_stop_sequence)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleApi->api_web_schedule_controller_index: %s\n" % e)
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
    api_instance = openapi_client.ScheduleApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key.  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/drop_off_type` | ascending | `drop_off_type` | | `/data/{index}/attributes/drop_off_type` | descending | `-drop_off_type` | | `/data/{index}/attributes/pickup_type` | ascending | `pickup_type` | | `/data/{index}/attributes/pickup_type` | descending | `-pickup_type` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` | | `/data/{index}/attributes/timepoint` | ascending | `timepoint` | | `/data/{index}/attributes/timepoint` | descending | `-timepoint` |  | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | ascending | `time` | | `/data/{index}/attributes/arrival_time` if present, otherwise `/data/{index}/attributes/departure_time` | descending | `-time` |   (optional)
fields_schedule = 'fields_schedule_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop` * `trip` * `prediction` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_date = '2013-10-20' # date | Filter schedule by date that they are active. The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_min_time = 'filter_min_time_example' # str | Time before which schedule should not be returned. To filter times after midnight use more than 24 hours. For example, min_time=24:00 will return schedule information for the next calendar day, since that service is considered part of the current service day. Additionally, min_time=00:00&max_time=02:00 will not return anything. The time format is HH:MM. (optional)
filter_max_time = 'filter_max_time_example' # str | Time after which schedule should not be returned. To filter times after midnight use more than 24 hours. For example, min_time=24:00 will return schedule information for the next calendar day, since that service is considered part of the current service day. Additionally, min_time=00:00&max_time=02:00 will not return anything. The time format is HH:MM. (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_stop_sequence = 'filter_stop_sequence_example' # str | Filter by the index of the stop in the trip.  Symbolic values `first` and `last` can be used instead of numeric sequence number too.  (optional)

    try:
        api_response = api_instance.api_web_schedule_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_schedule=fields_schedule, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_min_time=filter_min_time, filter_max_time=filter_max_time, filter_route=filter_route, filter_stop=filter_stop, filter_trip=filter_trip, filter_stop_sequence=filter_stop_sequence)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleApi->api_web_schedule_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key.  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/arrival_time&#x60; | ascending | &#x60;arrival_time&#x60; | | &#x60;/data/{index}/attributes/arrival_time&#x60; | descending | &#x60;-arrival_time&#x60; | | &#x60;/data/{index}/attributes/departure_time&#x60; | ascending | &#x60;departure_time&#x60; | | &#x60;/data/{index}/attributes/departure_time&#x60; | descending | &#x60;-departure_time&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/drop_off_type&#x60; | ascending | &#x60;drop_off_type&#x60; | | &#x60;/data/{index}/attributes/drop_off_type&#x60; | descending | &#x60;-drop_off_type&#x60; | | &#x60;/data/{index}/attributes/pickup_type&#x60; | ascending | &#x60;pickup_type&#x60; | | &#x60;/data/{index}/attributes/pickup_type&#x60; | descending | &#x60;-pickup_type&#x60; | | &#x60;/data/{index}/attributes/stop_sequence&#x60; | ascending | &#x60;stop_sequence&#x60; | | &#x60;/data/{index}/attributes/stop_sequence&#x60; | descending | &#x60;-stop_sequence&#x60; | | &#x60;/data/{index}/attributes/timepoint&#x60; | ascending | &#x60;timepoint&#x60; | | &#x60;/data/{index}/attributes/timepoint&#x60; | descending | &#x60;-timepoint&#x60; |  | &#x60;/data/{index}/attributes/arrival_time&#x60; if present, otherwise &#x60;/data/{index}/attributes/departure_time&#x60; | ascending | &#x60;time&#x60; | | &#x60;/data/{index}/attributes/arrival_time&#x60; if present, otherwise &#x60;/data/{index}/attributes/departure_time&#x60; | descending | &#x60;-time&#x60; |   | [optional] 
 **fields_schedule** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;stop&#x60; * &#x60;trip&#x60; * &#x60;prediction&#x60; * &#x60;route&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 
 **filter_date** | **date**| Filter schedule by date that they are active. The active date is the service date. Trips that begin between midnight and 3am are considered part of the previous service day. The format is ISO8601 with the template of YYYY-MM-DD. | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_min_time** | **str**| Time before which schedule should not be returned. To filter times after midnight use more than 24 hours. For example, min_time&#x3D;24:00 will return schedule information for the next calendar day, since that service is considered part of the current service day. Additionally, min_time&#x3D;00:00&amp;max_time&#x3D;02:00 will not return anything. The time format is HH:MM. | [optional] 
 **filter_max_time** | **str**| Time after which schedule should not be returned. To filter times after midnight use more than 24 hours. For example, min_time&#x3D;24:00 will return schedule information for the next calendar day, since that service is considered part of the current service day. Additionally, min_time&#x3D;00:00&amp;max_time&#x3D;02:00 will not return anything. The time format is HH:MM. | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_stop** | **str**| Filter by &#x60;/data/{index}/relationships/stop/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/stop/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_trip** | **str**| Filter by &#x60;/data/{index}/relationships/trip/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/trip/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_stop_sequence** | **str**| Filter by the index of the stop in the trip.  Symbolic values &#x60;first&#x60; and &#x60;last&#x60; can be used instead of numeric sequence number too.  | [optional] 

### Return type

[**Schedules**](Schedules.md)

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

