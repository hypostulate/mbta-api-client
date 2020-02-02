# openapi_client.ServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_service_controller_index**](ServiceApi.md#api_web_service_controller_index) | **GET** /services | 
[**api_web_service_controller_show**](ServiceApi.md#api_web_service_controller_show) | **GET** /services/{id} | 


# **api_web_service_controller_index**
> Services api_web_service_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_service=fields_service, filter_id=filter_id, filter_route=filter_route)



List of services. Service represents the days of the week, as well as extra days, that a trip is valid. 

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
    api_instance = openapi_client.ServiceApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/added_dates` | ascending | `added_dates` | | `/data/{index}/attributes/added_dates` | descending | `-added_dates` | | `/data/{index}/attributes/added_dates_notes` | ascending | `added_dates_notes` | | `/data/{index}/attributes/added_dates_notes` | descending | `-added_dates_notes` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/end_date` | ascending | `end_date` | | `/data/{index}/attributes/end_date` | descending | `-end_date` | | `/data/{index}/attributes/rating_description` | ascending | `rating_description` | | `/data/{index}/attributes/rating_description` | descending | `-rating_description` | | `/data/{index}/attributes/rating_end_date` | ascending | `rating_end_date` | | `/data/{index}/attributes/rating_end_date` | descending | `-rating_end_date` | | `/data/{index}/attributes/rating_start_date` | ascending | `rating_start_date` | | `/data/{index}/attributes/rating_start_date` | descending | `-rating_start_date` | | `/data/{index}/attributes/removed_dates` | ascending | `removed_dates` | | `/data/{index}/attributes/removed_dates` | descending | `-removed_dates` | | `/data/{index}/attributes/removed_dates_notes` | ascending | `removed_dates_notes` | | `/data/{index}/attributes/removed_dates_notes` | descending | `-removed_dates_notes` | | `/data/{index}/attributes/schedule_name` | ascending | `schedule_name` | | `/data/{index}/attributes/schedule_name` | descending | `-schedule_name` | | `/data/{index}/attributes/schedule_type` | ascending | `schedule_type` | | `/data/{index}/attributes/schedule_type` | descending | `-schedule_type` | | `/data/{index}/attributes/schedule_typicality` | ascending | `schedule_typicality` | | `/data/{index}/attributes/schedule_typicality` | descending | `-schedule_typicality` | | `/data/{index}/attributes/start_date` | ascending | `start_date` | | `/data/{index}/attributes/start_date` | descending | `-start_date` | | `/data/{index}/attributes/valid_days` | ascending | `valid_days` | | `/data/{index}/attributes/valid_days` | descending | `-valid_days` |   (optional)
fields_service = 'fields_service_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
filter_id = '1,2' # str | Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route = 'filter_route_example' # str | Filter by route. Multiple `route` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_service_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_service=fields_service, filter_id=filter_id, filter_route=filter_route)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceApi->api_web_service_controller_index: %s\n" % e)
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
    api_instance = openapi_client.ServiceApi(api_client)
    page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/added_dates` | ascending | `added_dates` | | `/data/{index}/attributes/added_dates` | descending | `-added_dates` | | `/data/{index}/attributes/added_dates_notes` | ascending | `added_dates_notes` | | `/data/{index}/attributes/added_dates_notes` | descending | `-added_dates_notes` | | `/data/{index}/attributes/description` | ascending | `description` | | `/data/{index}/attributes/description` | descending | `-description` | | `/data/{index}/attributes/end_date` | ascending | `end_date` | | `/data/{index}/attributes/end_date` | descending | `-end_date` | | `/data/{index}/attributes/rating_description` | ascending | `rating_description` | | `/data/{index}/attributes/rating_description` | descending | `-rating_description` | | `/data/{index}/attributes/rating_end_date` | ascending | `rating_end_date` | | `/data/{index}/attributes/rating_end_date` | descending | `-rating_end_date` | | `/data/{index}/attributes/rating_start_date` | ascending | `rating_start_date` | | `/data/{index}/attributes/rating_start_date` | descending | `-rating_start_date` | | `/data/{index}/attributes/removed_dates` | ascending | `removed_dates` | | `/data/{index}/attributes/removed_dates` | descending | `-removed_dates` | | `/data/{index}/attributes/removed_dates_notes` | ascending | `removed_dates_notes` | | `/data/{index}/attributes/removed_dates_notes` | descending | `-removed_dates_notes` | | `/data/{index}/attributes/schedule_name` | ascending | `schedule_name` | | `/data/{index}/attributes/schedule_name` | descending | `-schedule_name` | | `/data/{index}/attributes/schedule_type` | ascending | `schedule_type` | | `/data/{index}/attributes/schedule_type` | descending | `-schedule_type` | | `/data/{index}/attributes/schedule_typicality` | ascending | `schedule_typicality` | | `/data/{index}/attributes/schedule_typicality` | descending | `-schedule_typicality` | | `/data/{index}/attributes/start_date` | ascending | `start_date` | | `/data/{index}/attributes/start_date` | descending | `-start_date` | | `/data/{index}/attributes/valid_days` | ascending | `valid_days` | | `/data/{index}/attributes/valid_days` | descending | `-valid_days` |   (optional)
fields_service = 'fields_service_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)
filter_id = '1,2' # str | Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route = 'filter_route_example' # str | Filter by route. Multiple `route` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

    try:
        api_response = api_instance.api_web_service_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, fields_service=fields_service, filter_id=filter_id, filter_route=filter_route)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceApi->api_web_service_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/added_dates&#x60; | ascending | &#x60;added_dates&#x60; | | &#x60;/data/{index}/attributes/added_dates&#x60; | descending | &#x60;-added_dates&#x60; | | &#x60;/data/{index}/attributes/added_dates_notes&#x60; | ascending | &#x60;added_dates_notes&#x60; | | &#x60;/data/{index}/attributes/added_dates_notes&#x60; | descending | &#x60;-added_dates_notes&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | ascending | &#x60;description&#x60; | | &#x60;/data/{index}/attributes/description&#x60; | descending | &#x60;-description&#x60; | | &#x60;/data/{index}/attributes/end_date&#x60; | ascending | &#x60;end_date&#x60; | | &#x60;/data/{index}/attributes/end_date&#x60; | descending | &#x60;-end_date&#x60; | | &#x60;/data/{index}/attributes/rating_description&#x60; | ascending | &#x60;rating_description&#x60; | | &#x60;/data/{index}/attributes/rating_description&#x60; | descending | &#x60;-rating_description&#x60; | | &#x60;/data/{index}/attributes/rating_end_date&#x60; | ascending | &#x60;rating_end_date&#x60; | | &#x60;/data/{index}/attributes/rating_end_date&#x60; | descending | &#x60;-rating_end_date&#x60; | | &#x60;/data/{index}/attributes/rating_start_date&#x60; | ascending | &#x60;rating_start_date&#x60; | | &#x60;/data/{index}/attributes/rating_start_date&#x60; | descending | &#x60;-rating_start_date&#x60; | | &#x60;/data/{index}/attributes/removed_dates&#x60; | ascending | &#x60;removed_dates&#x60; | | &#x60;/data/{index}/attributes/removed_dates&#x60; | descending | &#x60;-removed_dates&#x60; | | &#x60;/data/{index}/attributes/removed_dates_notes&#x60; | ascending | &#x60;removed_dates_notes&#x60; | | &#x60;/data/{index}/attributes/removed_dates_notes&#x60; | descending | &#x60;-removed_dates_notes&#x60; | | &#x60;/data/{index}/attributes/schedule_name&#x60; | ascending | &#x60;schedule_name&#x60; | | &#x60;/data/{index}/attributes/schedule_name&#x60; | descending | &#x60;-schedule_name&#x60; | | &#x60;/data/{index}/attributes/schedule_type&#x60; | ascending | &#x60;schedule_type&#x60; | | &#x60;/data/{index}/attributes/schedule_type&#x60; | descending | &#x60;-schedule_type&#x60; | | &#x60;/data/{index}/attributes/schedule_typicality&#x60; | ascending | &#x60;schedule_typicality&#x60; | | &#x60;/data/{index}/attributes/schedule_typicality&#x60; | descending | &#x60;-schedule_typicality&#x60; | | &#x60;/data/{index}/attributes/start_date&#x60; | ascending | &#x60;start_date&#x60; | | &#x60;/data/{index}/attributes/start_date&#x60; | descending | &#x60;-start_date&#x60; | | &#x60;/data/{index}/attributes/valid_days&#x60; | ascending | &#x60;valid_days&#x60; | | &#x60;/data/{index}/attributes/valid_days&#x60; | descending | &#x60;-valid_days&#x60; |   | [optional] 
 **fields_service** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 
 **filter_id** | **str**| Filter by multiple IDs. **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_route** | **str**| Filter by route. Multiple &#x60;route&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**Services**](Services.md)

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

# **api_web_service_controller_show**
> Service api_web_service_controller_show(id, fields_service=fields_service)



Single service, which represents the days of the week, as well as extra days, that a trip is valid. 

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
    api_instance = openapi_client.ServiceApi(api_client)
    id = 'id_example' # str | Unique identifier for a service
fields_service = 'fields_service_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)

    try:
        api_response = api_instance.api_web_service_controller_show(id, fields_service=fields_service)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceApi->api_web_service_controller_show: %s\n" % e)
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
    api_instance = openapi_client.ServiceApi(api_client)
    id = 'id_example' # str | Unique identifier for a service
fields_service = 'fields_service_example' # str | Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \",\") list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  (optional)

    try:
        api_response = api_instance.api_web_service_controller_show(id, fields_service=fields_service)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceApi->api_web_service_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a service | 
 **fields_service** | **str**| Fields to include with the response. Multiple fields **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  Note that fields can also be selected for included data types: see the [V3 API Best Practices](https://www.mbta.com/developers/v3-api/best-practices) for an example.  | [optional] 

### Return type

[**Service**](Service.md)

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

