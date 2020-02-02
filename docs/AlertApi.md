# openapi_client.AlertApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_alert_controller_index**](AlertApi.md#api_web_alert_controller_index) | **GET** /alerts | 
[**api_web_alert_controller_show**](AlertApi.md#api_web_alert_controller_show) | **GET** /alerts/{id} | 


# **api_web_alert_controller_index**
> Alerts api_web_alert_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_alert=fields_alert, include=include, filter_activity=filter_activity, filter_route_type=filter_route_type, filter_direction_id=filter_direction_id, filter_route=filter_route, filter_stop=filter_stop, filter_trip=filter_trip, filter_facility=filter_facility, filter_id=filter_id, filter_banner=filter_banner, filter_datetime=filter_datetime, filter_lifecycle=filter_lifecycle, filter_severity=filter_severity)



List active and upcoming system alerts  An effect (enumerated in `/data/{index}/attributes/effect` and human-readable in `/data/{index}/attributes/service_effect`) on a provided service (facility, route, route type, stop and/or trip in `//data/{index}/attributes/informed_entity`) described by a banner (`/data/{index}/attributes/banner`), short header (`/data/{index}/attributes/short_header`), header `/data/{index}/attributes/header`, and description (`/data/{index}/attributes/description`) that is active for one or more periods (`/data/{index}/attributes/active_period`) caused by a cause (`/data/{index}/attribute/cause`) that somewhere in its lifecycle (enumerated in `/data/{index}/attributes/lifecycle` and human-readable in `/data/{index}/attributes/timeframe`).  See [GTFS Realtime `FeedMessage` `FeedEntity` `Alert`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-alert)  ## Descriptions  There are 5 descriptive attributes.  | JSON pointer                                | Usage                                                                           | |---------------------------------------------|---------------------------------------------------------------------------------| | `/data/{index}/attributes/banner`       | Display as alert across application/website                                     | | `/data/{index}/attributes/short_header` | When `/data/{index}/attributes/header` is too long to display               | | `/data/{index}/attributes/header`       | Used before showing and prepended to `/data/{index}/attributes/description` | | `/data/{index}/attributes/description`  | Used when user asks to expand alert.                                            |  ## Effect  | JSON pointer                                  |                | |-----------------------------------------------|----------------| | `/data/{index}/attributes/effect`         | Enumerated     | | `/data/{index}/attributes/service_effect` | Human-readable |  ## Timeline  There are 3 timeline related attributes  | JSON pointer                                 | Description                                                                              | |----------------------------------------------|------------------------------------------------------------------------------------------| | `/data/{index}/attributes/active_period` | Exact Date/Time ranges alert is active                                                   | | `/data/{index}/attributes/lifecycle`     | Enumerated, machine-readable description of `/data/{index}/attributes/active_period` | | `/data/{index}/attributes/timeframe`     | Human-readable description of `/data/{index}/attributes/active_period`               |   ## Activities  Alerts are by default filtered to those where `/data/{index}/attributes/informed_entity/{informed_entity_index}/activities/{activity_index}` in one of BOARDEXITRIDE, as these cover most riders.  If you want all alerts without filtering by activity, you should use the special value `\"ALL\"`: `filter[activity]=ALL`.  ### Accessibility  The default activities cover if boarding, exiting, or riding is generally affected for all riders by the alert. If ONLY wheelchair using riders are affected, such as if a ramp, lift, or safety system for wheelchairs is affected, only the `\"USING_WHEELCHAIR\"` activity will be set. To cover wheelchair using rider, filter on the defaults and `\"USING_WHEELCHAIR\"`: `filter[activity]=USING_WHEELCHAIR,BOARD,EXIT,RIDE`.  Similarly for riders with limited mobility that need escalators, `\"USING_ESCALATOR\"` should be added to the defaults: `filter[activity]=USING_ESCALATOR,BOARD,EXIT,RIDE`.  

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
    api_instance = openapi_client.AlertApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/active_period` | ascending | `active_period` | | `/data/{index}/attributes/active_period` | descending | `-active_period` | | `/data/{index}/attributes/banner` | ascending | `banner` | | `/data/{index}/attributes/banner` | descending | `-banner` | | `/data/{index}/attributes/cause` | ascending | `cause` | | `/data/{index}/attributes/cause` | descending | `-cause` | | `/data/{index}/attributes/created_at` | ascending | `created_at` | | `/data/{index}/attributes/created_at` | descending | `-created_at` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/effect` | ascending | `effect` | | `/data/{index}/attributes/effect` | descending | `-effect` | | `/data/{index}/attributes/effect_name` | ascending | `effect_name` | | `/data/{index}/attributes/effect_name` | descending | `-effect_name` | | `/data/{index}/attributes/header` | ascending | `header` | | `/data/{index}/attributes/header` | descending | `-header` | | `/data/{index}/attributes/informed_entity` | ascending | `informed_entity` | | `/data/{index}/attributes/informed_entity` | descending | `-informed_entity` | | `/data/{index}/attributes/lifecycle` | ascending | `lifecycle` | | `/data/{index}/attributes/lifecycle` | descending | `-lifecycle` | | `/data/{index}/attributes/service_effect` | ascending | `service_effect` | | `/data/{index}/attributes/service_effect` | descending | `-service_effect` | | `/data/{index}/attributes/severity` | ascending | `severity` | | `/data/{index}/attributes/severity` | descending | `-severity` | | `/data/{index}/attributes/short_header` | ascending | `short_header` | | `/data/{index}/attributes/short_header` | descending | `-short_header` | | `/data/{index}/attributes/timeframe` | ascending | `timeframe` | | `/data/{index}/attributes/timeframe` | descending | `-timeframe` | | `/data/{index}/attributes/updated_at` | ascending | `updated_at` | | `/data/{index}/attributes/updated_at` | descending | `-updated_at` | | `/data/{index}/attributes/url` | ascending | `url` | | `/data/{index}/attributes/url` | descending | `-url` |   (optional)
fields_alert = 'fields_alert_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stops` * `routes` * `trips` * `facilities`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_activity = 'BOARD,EXIT,RIDE' # str | Filter to alerts for only those activities (`/data/{index}/attributes/informed_entity/activities/{activity_index}`) matching.  Multiple activities **MUST** be a comma-separated (U+002C COMMA, \",\") list.  An activity affected by an alert.  | Value                | Description                                                                                                                                                                                                                                                                       | |----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `\"BOARD\"`            | Boarding a vehicle. Any passenger trip includes boarding a vehicle and exiting from a vehicle.                                                                                                                                                                                    | | `\"BRINGING_BIKE\"`    | Bringing a bicycle while boarding or exiting.                                                                                                                                                                                                                                     | | `\"EXIT\"`             | Exiting from a vehicle (disembarking). Any passenger trip includes boarding a vehicle and exiting a vehicle.                                                                                                                                                                      | | `\"PARK_CAR\"`         | Parking a car at a garage or lot in a station.                                                                                                                                                                                                                                    | | `\"RIDE\"`             | Riding through a stop without boarding or exiting.. Not every passenger trip will include this -- a passenger may board at one stop and exit at the next stop.                                                                                                                    | | `\"STORE_BIKE\"`       | Storing a bicycle at a station.                                                                                                                                                                                                                                                   | | `\"USING_ESCALATOR\"`  | Using an escalator while boarding or exiting (should only be used for customers who specifically want to avoid stairs.)                                                                                                                                                           | | `\"USING_WHEELCHAIR\"` | Using a wheelchair while boarding or exiting. Note that this applies to something that specifically affects customers who use a wheelchair to board or exit; a delay should not include this as an affected activity unless it specifically affects customers using wheelchairs.  |   ## Special Values  * If the filter is not given OR it is empty, then defaults to [\"BOARD\", \"EXIT\", \"RIDE\"]. * If the value `\"ALL\"` is used then all alerts will be returned, not just those with the default activities.  ## Accessibility  The default activities cover if boarding, exiting, or riding is generally affected for all riders by the alert. If ONLY wheelchair using riders are affected, such as if a ramp, lift, or safety system for wheelchairs is affected, only the `\"USING_WHEELCHAIR\"` activity will be set. To cover wheelchair using rider, filter on the defaults and `\"USING_WHEELCHAIR\"`: `filter[activity]=USING_WHEELCHAIR,BOARD,EXIT,RIDE`.  Similarly for riders with limited mobility that need escalators, `\"USING_ESCALATOR\"` should be added to the defaults: `filter[activity]=USING_ESCALATOR,BOARD,EXIT,RIDE`.   (optional) (default to 'BOARD,EXIT,RIDE')
filter_route_type = 'filter_route_type_example' # str | Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_facility = 'filter_facility_example' # str | Filter by `/data/{index}/relationships/facility/data/id`. Multiple `/data/{index}/relationships/facility/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_id = '1,2' # str | Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_banner = 'true' # str | When combined with other filters, filters by alerts with or without a banner. **MUST** be \"true\" or \"false\".  (optional)
filter_datetime = '2018-05-09T13:06:00-04:00' # str | Filter to alerts that are active at a given time (ISO8601 format).  Additionally, the string \"NOW\" can be used to filter to alerts that are currently active.  (optional)
filter_lifecycle = 'filter_lifecycle_example' # str | Filters by an alert's lifecycle. **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_severity = 'filter_severity_example' # str | Filters alerts by list of severities. **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Example: filter[severity]=3,4,10 returns alerts with severity levels 3, 4 and 10.  (optional)

    try:
        api_response = api_instance.api_web_alert_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_alert=fields_alert, include=include, filter_activity=filter_activity, filter_route_type=filter_route_type, filter_direction_id=filter_direction_id, filter_route=filter_route, filter_stop=filter_stop, filter_trip=filter_trip, filter_facility=filter_facility, filter_id=filter_id, filter_banner=filter_banner, filter_datetime=filter_datetime, filter_lifecycle=filter_lifecycle, filter_severity=filter_severity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->api_web_alert_controller_index: %s\n" % e)
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
    api_instance = openapi_client.AlertApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/active_period` | ascending | `active_period` | | `/data/{index}/attributes/active_period` | descending | `-active_period` | | `/data/{index}/attributes/banner` | ascending | `banner` | | `/data/{index}/attributes/banner` | descending | `-banner` | | `/data/{index}/attributes/cause` | ascending | `cause` | | `/data/{index}/attributes/cause` | descending | `-cause` | | `/data/{index}/attributes/created_at` | ascending | `created_at` | | `/data/{index}/attributes/created_at` | descending | `-created_at` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/effect` | ascending | `effect` | | `/data/{index}/attributes/effect` | descending | `-effect` | | `/data/{index}/attributes/effect_name` | ascending | `effect_name` | | `/data/{index}/attributes/effect_name` | descending | `-effect_name` | | `/data/{index}/attributes/header` | ascending | `header` | | `/data/{index}/attributes/header` | descending | `-header` | | `/data/{index}/attributes/informed_entity` | ascending | `informed_entity` | | `/data/{index}/attributes/informed_entity` | descending | `-informed_entity` | | `/data/{index}/attributes/lifecycle` | ascending | `lifecycle` | | `/data/{index}/attributes/lifecycle` | descending | `-lifecycle` | | `/data/{index}/attributes/service_effect` | ascending | `service_effect` | | `/data/{index}/attributes/service_effect` | descending | `-service_effect` | | `/data/{index}/attributes/severity` | ascending | `severity` | | `/data/{index}/attributes/severity` | descending | `-severity` | | `/data/{index}/attributes/short_header` | ascending | `short_header` | | `/data/{index}/attributes/short_header` | descending | `-short_header` | | `/data/{index}/attributes/timeframe` | ascending | `timeframe` | | `/data/{index}/attributes/timeframe` | descending | `-timeframe` | | `/data/{index}/attributes/updated_at` | ascending | `updated_at` | | `/data/{index}/attributes/updated_at` | descending | `-updated_at` | | `/data/{index}/attributes/url` | ascending | `url` | | `/data/{index}/attributes/url` | descending | `-url` |   (optional)
fields_alert = 'fields_alert_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stops` * `routes` * `trips` * `facilities`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_activity = 'BOARD,EXIT,RIDE' # str | Filter to alerts for only those activities (`/data/{index}/attributes/informed_entity/activities/{activity_index}`) matching.  Multiple activities **MUST** be a comma-separated (U+002C COMMA, \",\") list.  An activity affected by an alert.  | Value                | Description                                                                                                                                                                                                                                                                       | |----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `\"BOARD\"`            | Boarding a vehicle. Any passenger trip includes boarding a vehicle and exiting from a vehicle.                                                                                                                                                                                    | | `\"BRINGING_BIKE\"`    | Bringing a bicycle while boarding or exiting.                                                                                                                                                                                                                                     | | `\"EXIT\"`             | Exiting from a vehicle (disembarking). Any passenger trip includes boarding a vehicle and exiting a vehicle.                                                                                                                                                                      | | `\"PARK_CAR\"`         | Parking a car at a garage or lot in a station.                                                                                                                                                                                                                                    | | `\"RIDE\"`             | Riding through a stop without boarding or exiting.. Not every passenger trip will include this -- a passenger may board at one stop and exit at the next stop.                                                                                                                    | | `\"STORE_BIKE\"`       | Storing a bicycle at a station.                                                                                                                                                                                                                                                   | | `\"USING_ESCALATOR\"`  | Using an escalator while boarding or exiting (should only be used for customers who specifically want to avoid stairs.)                                                                                                                                                           | | `\"USING_WHEELCHAIR\"` | Using a wheelchair while boarding or exiting. Note that this applies to something that specifically affects customers who use a wheelchair to board or exit; a delay should not include this as an affected activity unless it specifically affects customers using wheelchairs.  |   ## Special Values  * If the filter is not given OR it is empty, then defaults to [\"BOARD\", \"EXIT\", \"RIDE\"]. * If the value `\"ALL\"` is used then all alerts will be returned, not just those with the default activities.  ## Accessibility  The default activities cover if boarding, exiting, or riding is generally affected for all riders by the alert. If ONLY wheelchair using riders are affected, such as if a ramp, lift, or safety system for wheelchairs is affected, only the `\"USING_WHEELCHAIR\"` activity will be set. To cover wheelchair using rider, filter on the defaults and `\"USING_WHEELCHAIR\"`: `filter[activity]=USING_WHEELCHAIR,BOARD,EXIT,RIDE`.  Similarly for riders with limited mobility that need escalators, `\"USING_ESCALATOR\"` should be added to the defaults: `filter[activity]=USING_ESCALATOR,BOARD,EXIT,RIDE`.   (optional) (default to 'BOARD,EXIT,RIDE')
filter_route_type = 'filter_route_type_example' # str | Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple `route_type` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_facility = 'filter_facility_example' # str | Filter by `/data/{index}/relationships/facility/data/id`. Multiple `/data/{index}/relationships/facility/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_id = '1,2' # str | Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_banner = 'true' # str | When combined with other filters, filters by alerts with or without a banner. **MUST** be \"true\" or \"false\".  (optional)
filter_datetime = '2018-05-09T13:06:00-04:00' # str | Filter to alerts that are active at a given time (ISO8601 format).  Additionally, the string \"NOW\" can be used to filter to alerts that are currently active.  (optional)
filter_lifecycle = 'filter_lifecycle_example' # str | Filters by an alert's lifecycle. **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_severity = 'filter_severity_example' # str | Filters alerts by list of severities. **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Example: filter[severity]=3,4,10 returns alerts with severity levels 3, 4 and 10.  (optional)

    try:
        api_response = api_instance.api_web_alert_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_alert=fields_alert, include=include, filter_activity=filter_activity, filter_route_type=filter_route_type, filter_direction_id=filter_direction_id, filter_route=filter_route, filter_stop=filter_stop, filter_trip=filter_trip, filter_facility=filter_facility, filter_id=filter_id, filter_banner=filter_banner, filter_datetime=filter_datetime, filter_lifecycle=filter_lifecycle, filter_severity=filter_severity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->api_web_alert_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/active_period&#x60; | ascending | &#x60;active_period&#x60; | | &#x60;/data/{index}/attributes/active_period&#x60; | descending | &#x60;-active_period&#x60; | | &#x60;/data/{index}/attributes/banner&#x60; | ascending | &#x60;banner&#x60; | | &#x60;/data/{index}/attributes/banner&#x60; | descending | &#x60;-banner&#x60; | | &#x60;/data/{index}/attributes/cause&#x60; | ascending | &#x60;cause&#x60; | | &#x60;/data/{index}/attributes/cause&#x60; | descending | &#x60;-cause&#x60; | | &#x60;/data/{index}/attributes/created_at&#x60; | ascending | &#x60;created_at&#x60; | | &#x60;/data/{index}/attributes/created_at&#x60; | descending | &#x60;-created_at&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | ascending | &#x60;description&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | descending | &#x60;-description&#x60; | | &#x60;/data/{index}/attributes/effect&#x60; | ascending | &#x60;effect&#x60; | | &#x60;/data/{index}/attributes/effect&#x60; | descending | &#x60;-effect&#x60; | | &#x60;/data/{index}/attributes/effect_name&#x60; | ascending | &#x60;effect_name&#x60; | | &#x60;/data/{index}/attributes/effect_name&#x60; | descending | &#x60;-effect_name&#x60; | | &#x60;/data/{index}/attributes/header&#x60; | ascending | &#x60;header&#x60; | | &#x60;/data/{index}/attributes/header&#x60; | descending | &#x60;-header&#x60; | | &#x60;/data/{index}/attributes/informed_entity&#x60; | ascending | &#x60;informed_entity&#x60; | | &#x60;/data/{index}/attributes/informed_entity&#x60; | descending | &#x60;-informed_entity&#x60; | | &#x60;/data/{index}/attributes/lifecycle&#x60; | ascending | &#x60;lifecycle&#x60; | | &#x60;/data/{index}/attributes/lifecycle&#x60; | descending | &#x60;-lifecycle&#x60; | | &#x60;/data/{index}/attributes/service_effect&#x60; | ascending | &#x60;service_effect&#x60; | | &#x60;/data/{index}/attributes/service_effect&#x60; | descending | &#x60;-service_effect&#x60; | | &#x60;/data/{index}/attributes/severity&#x60; | ascending | &#x60;severity&#x60; | | &#x60;/data/{index}/attributes/severity&#x60; | descending | &#x60;-severity&#x60; | | &#x60;/data/{index}/attributes/short_header&#x60; | ascending | &#x60;short_header&#x60; | | &#x60;/data/{index}/attributes/short_header&#x60; | descending | &#x60;-short_header&#x60; | | &#x60;/data/{index}/attributes/timeframe&#x60; | ascending | &#x60;timeframe&#x60; | | &#x60;/data/{index}/attributes/timeframe&#x60; | descending | &#x60;-timeframe&#x60; | | &#x60;/data/{index}/attributes/updated_at&#x60; | ascending | &#x60;updated_at&#x60; | | &#x60;/data/{index}/attributes/updated_at&#x60; | descending | &#x60;-updated_at&#x60; | | &#x60;/data/{index}/attributes/url&#x60; | ascending | &#x60;url&#x60; | | &#x60;/data/{index}/attributes/url&#x60; | descending | &#x60;-url&#x60; |   | [optional] 
 **fields_alert** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;stops&#x60; * &#x60;routes&#x60; * &#x60;trips&#x60; * &#x60;facilities&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 
 **filter_activity** | **str**| Filter to alerts for only those activities (&#x60;/data/{index}/attributes/informed_entity/activities/{activity_index}&#x60;) matching.  Multiple activities **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  An activity affected by an alert.  | Value                | Description                                                                                                                                                                                                                                                                       | |----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | &#x60;\&quot;BOARD\&quot;&#x60;            | Boarding a vehicle. Any passenger trip includes boarding a vehicle and exiting from a vehicle.                                                                                                                                                                                    | | &#x60;\&quot;BRINGING_BIKE\&quot;&#x60;    | Bringing a bicycle while boarding or exiting.                                                                                                                                                                                                                                     | | &#x60;\&quot;EXIT\&quot;&#x60;             | Exiting from a vehicle (disembarking). Any passenger trip includes boarding a vehicle and exiting a vehicle.                                                                                                                                                                      | | &#x60;\&quot;PARK_CAR\&quot;&#x60;         | Parking a car at a garage or lot in a station.                                                                                                                                                                                                                                    | | &#x60;\&quot;RIDE\&quot;&#x60;             | Riding through a stop without boarding or exiting.. Not every passenger trip will include this -- a passenger may board at one stop and exit at the next stop.                                                                                                                    | | &#x60;\&quot;STORE_BIKE\&quot;&#x60;       | Storing a bicycle at a station.                                                                                                                                                                                                                                                   | | &#x60;\&quot;USING_ESCALATOR\&quot;&#x60;  | Using an escalator while boarding or exiting (should only be used for customers who specifically want to avoid stairs.)                                                                                                                                                           | | &#x60;\&quot;USING_WHEELCHAIR\&quot;&#x60; | Using a wheelchair while boarding or exiting. Note that this applies to something that specifically affects customers who use a wheelchair to board or exit; a delay should not include this as an affected activity unless it specifically affects customers using wheelchairs.  |   ## Special Values  * If the filter is not given OR it is empty, then defaults to [\&quot;BOARD\&quot;, \&quot;EXIT\&quot;, \&quot;RIDE\&quot;]. * If the value &#x60;\&quot;ALL\&quot;&#x60; is used then all alerts will be returned, not just those with the default activities.  ## Accessibility  The default activities cover if boarding, exiting, or riding is generally affected for all riders by the alert. If ONLY wheelchair using riders are affected, such as if a ramp, lift, or safety system for wheelchairs is affected, only the &#x60;\&quot;USING_WHEELCHAIR\&quot;&#x60; activity will be set. To cover wheelchair using rider, filter on the defaults and &#x60;\&quot;USING_WHEELCHAIR\&quot;&#x60;: &#x60;filter[activity]&#x3D;USING_WHEELCHAIR,BOARD,EXIT,RIDE&#x60;.  Similarly for riders with limited mobility that need escalators, &#x60;\&quot;USING_ESCALATOR\&quot;&#x60; should be added to the defaults: &#x60;filter[activity]&#x3D;USING_ESCALATOR,BOARD,EXIT,RIDE&#x60;.   | [optional] [default to &#39;BOARD,EXIT,RIDE&#39;]
 **filter_route_type** | **str**| Filter by route_type: https://developers.google.com/transit/gtfs/reference/routes-file.  Multiple &#x60;route_type&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_stop** | **str**| Filter by &#x60;/data/{index}/relationships/stop/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/stop/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_trip** | **str**| Filter by &#x60;/data/{index}/relationships/trip/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/trip/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_facility** | **str**| Filter by &#x60;/data/{index}/relationships/facility/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/facility/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_id** | **str**| Filter by multiple IDs. Multiple IDs **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_banner** | **str**| When combined with other filters, filters by alerts with or without a banner. **MUST** be \&quot;true\&quot; or \&quot;false\&quot;.  | [optional] 
 **filter_datetime** | **str**| Filter to alerts that are active at a given time (ISO8601 format).  Additionally, the string \&quot;NOW\&quot; can be used to filter to alerts that are currently active.  | [optional] 
 **filter_lifecycle** | **str**| Filters by an alert&#39;s lifecycle. **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_severity** | **str**| Filters alerts by list of severities. **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Example: filter[severity]&#x3D;3,4,10 returns alerts with severity levels 3, 4 and 10.  | [optional] 

### Return type

[**Alerts**](Alerts.md)

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

# **api_web_alert_controller_show**
> Alert api_web_alert_controller_show(id, fields_alert=fields_alert, include=include)



Show a particular alert by the alert's id  An effect (enumerated in `/data/attributes/effect` and human-readable in `/data/attributes/service_effect`) on a provided service (facility, route, route type, stop and/or trip in `//data/attributes/informed_entity`) described by a banner (`/data/attributes/banner`), short header (`/data/attributes/short_header`), header `/data/attributes/header`, and description (`/data/attributes/description`) that is active for one or more periods (`/data/attributes/active_period`) caused by a cause (`/data/attribute/cause`) that somewhere in its lifecycle (enumerated in `/data/attributes/lifecycle` and human-readable in `/data/attributes/timeframe`).  See [GTFS Realtime `FeedMessage` `FeedEntity` `Alert`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-alert)  ## Descriptions  There are 5 descriptive attributes.  | JSON pointer                                | Usage                                                                           | |---------------------------------------------|---------------------------------------------------------------------------------| | `/data/attributes/banner`       | Display as alert across application/website                                     | | `/data/attributes/short_header` | When `/data/attributes/header` is too long to display               | | `/data/attributes/header`       | Used before showing and prepended to `/data/attributes/description` | | `/data/attributes/description`  | Used when user asks to expand alert.                                            |  ## Effect  | JSON pointer                                  |                | |-----------------------------------------------|----------------| | `/data/attributes/effect`         | Enumerated     | | `/data/attributes/service_effect` | Human-readable |  ## Timeline  There are 3 timeline related attributes  | JSON pointer                                 | Description                                                                              | |----------------------------------------------|------------------------------------------------------------------------------------------| | `/data/attributes/active_period` | Exact Date/Time ranges alert is active                                                   | | `/data/attributes/lifecycle`     | Enumerated, machine-readable description of `/data/attributes/active_period` | | `/data/attributes/timeframe`     | Human-readable description of `/data/attributes/active_period`               |  

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
    api_instance = openapi_client.AlertApi(api_client)
    id = 'id_example' # str | Unique identifier for alert
fields_alert = 'fields_alert_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stops` * `routes` * `trips` * `facilities`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

    try:
        api_response = api_instance.api_web_alert_controller_show(id, fields_alert=fields_alert, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->api_web_alert_controller_show: %s\n" % e)
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
    api_instance = openapi_client.AlertApi(api_client)
    id = 'id_example' # str | Unique identifier for alert
fields_alert = 'fields_alert_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stops` * `routes` * `trips` * `facilities`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

    try:
        api_response = api_instance.api_web_alert_controller_show(id, fields_alert=fields_alert, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertApi->api_web_alert_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for alert | 
 **fields_alert** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;stops&#x60; * &#x60;routes&#x60; * &#x60;trips&#x60; * &#x60;facilities&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 

### Return type

[**Alert**](Alert.md)

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

