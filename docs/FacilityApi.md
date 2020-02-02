# openapi_client.FacilityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_facility_controller_index**](FacilityApi.md#api_web_facility_controller_index) | **GET** /facilities | 
[**api_web_facility_controller_show**](FacilityApi.md#api_web_facility_controller_show) | **GET** /facilities/{id} | 


# **api_web_facility_controller_index**
> Facilities api_web_facility_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_facility=fields_facility, include=include, filter_stop=filter_stop, filter_type=filter_type)



List Escalators and Elevators  Amenities at a station stop (`/data/relationships/stop`) such as elevators, escalators, parking lots, and bike storage.  An [MBTA extension](https://groups.google.com/forum/#!topic/gtfs-changes/EzC5m9k45pA).  This spec is not yet finalized.  ## Accessibility  Riders with limited mobility can search any facility, either `ELEVATOR` or `ESCALATOR`, while riders that need wheelchair access can search for `ELEVATOR` only.  The lack of an `ELEVATOR` MAY NOT make a stop wheelchair inaccessible.  Riders should check `/stops/{id}` `/data/attributes/wheelchair_boarding` is `1` to guarantee a path is available from the station entrance to the stop or `0` if it MAY be accessible.  Completely avoid `2` as that is guaranteed to be INACCESSIBLE.  

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
    api_instance = openapi_client.FacilityApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/long_name` | ascending | `long_name` | | `/data/{index}/attributes/long_name` | descending | `-long_name` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/properties` | ascending | `properties` | | `/data/{index}/attributes/properties` | descending | `-properties` | | `/data/{index}/attributes/short_name` | ascending | `short_name` | | `/data/{index}/attributes/short_name` | descending | `-short_name` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |   (optional)
fields_facility = 'fields_facility_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_type = 'filter_type_example' # str | Filter by multiple types.  Multiple types **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_facility_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_facility=fields_facility, include=include, filter_stop=filter_stop, filter_type=filter_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FacilityApi->api_web_facility_controller_index: %s\n" % e)
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
    api_instance = openapi_client.FacilityApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/long_name` | ascending | `long_name` | | `/data/{index}/attributes/long_name` | descending | `-long_name` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/properties` | ascending | `properties` | | `/data/{index}/attributes/properties` | descending | `-properties` | | `/data/{index}/attributes/short_name` | ascending | `short_name` | | `/data/{index}/attributes/short_name` | descending | `-short_name` | | `/data/{index}/attributes/type` | ascending | `type` | | `/data/{index}/attributes/type` | descending | `-type` |   (optional)
fields_facility = 'fields_facility_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_type = 'filter_type_example' # str | Filter by multiple types.  Multiple types **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_facility_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_facility=fields_facility, include=include, filter_stop=filter_stop, filter_type=filter_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FacilityApi->api_web_facility_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/latitude&#x60; | ascending | &#x60;latitude&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | descending | &#x60;-latitude&#x60; | | &#x60;/data/{index}/attributes/long_name&#x60; | ascending | &#x60;long_name&#x60; | | &#x60;/data/{index}/attributes/long_name&#x60; | descending | &#x60;-long_name&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | ascending | &#x60;longitude&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | descending | &#x60;-longitude&#x60; | | &#x60;/data/{index}/attributes/properties&#x60; | ascending | &#x60;properties&#x60; | | &#x60;/data/{index}/attributes/properties&#x60; | descending | &#x60;-properties&#x60; | | &#x60;/data/{index}/attributes/short_name&#x60; | ascending | &#x60;short_name&#x60; | | &#x60;/data/{index}/attributes/short_name&#x60; | descending | &#x60;-short_name&#x60; | | &#x60;/data/{index}/attributes/type&#x60; | ascending | &#x60;type&#x60; | | &#x60;/data/{index}/attributes/type&#x60; | descending | &#x60;-type&#x60; |   | [optional] 
 **fields_facility** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;stop&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 
 **filter_stop** | **str**| Filter by &#x60;/data/{index}/relationships/stop/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/stop/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_type** | **str**| Filter by multiple types.  Multiple types **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**Facilities**](Facilities.md)

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

# **api_web_facility_controller_show**
> Facility api_web_facility_controller_show(id, fields_facility=fields_facility, include=include)



Specific Escalator or Elevator  Amenities at a station stop (`/data/{index}/relationships/stop`) such as elevators, escalators, parking lots, and bike storage.  An [MBTA extension](https://groups.google.com/forum/#!topic/gtfs-changes/EzC5m9k45pA).  This spec is not yet finalized.  ## Accessibility  Riders with limited mobility can search any facility, either `ELEVATOR` or `ESCALATOR`, while riders that need wheelchair access can search for `ELEVATOR` only.  The lack of an `ELEVATOR` MAY NOT make a stop wheelchair inaccessible.  Riders should check `/stops/{id}` `/data/attributes/wheelchair_boarding` is `1` to guarantee a path is available from the station entrance to the stop or `0` if it MAY be accessible.  Completely avoid `2` as that is guaranteed to be INACCESSIBLE.  

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
    api_instance = openapi_client.FacilityApi(api_client)
    id = 'id_example' # str | Unique identifier for facility
fields_facility = 'fields_facility_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

    try:
        api_response = api_instance.api_web_facility_controller_show(id, fields_facility=fields_facility, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FacilityApi->api_web_facility_controller_show: %s\n" % e)
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
    api_instance = openapi_client.FacilityApi(api_client)
    id = 'id_example' # str | Unique identifier for facility
fields_facility = 'fields_facility_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
include = 'include_example' # str | Relationships to include.  * `stop`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

    try:
        api_response = api_instance.api_web_facility_controller_show(id, fields_facility=fields_facility, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FacilityApi->api_web_facility_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for facility | 
 **fields_facility** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;stop&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 

### Return type

[**Facility**](Facility.md)

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

