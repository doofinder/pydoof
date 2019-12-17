# pydoof2.StatsApi

All URIs are relative to *https://eu1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banners_clicks**](StatsApi.md#banners_clicks) | **GET** /api/v2/stats/banners/clicks | Get the total amount of clicks banners have got
[**banners_display**](StatsApi.md#banners_display) | **GET** /api/v2/stats/banners/display | Get the total amount of displays banners have got
[**checkouts**](StatsApi.md#checkouts) | **GET** /api/v2/stats/checkouts | Get total checkouts
[**checkouts_by_date**](StatsApi.md#checkouts_by_date) | **GET** /api/v2/stats/checkouts/by-date | Get the checkouts by dates
[**clicks**](StatsApi.md#clicks) | **GET** /api/v2/stats/clicks | Get total clicks
[**clicks_by_date**](StatsApi.md#clicks_by_date) | **GET** /api/v2/stats/clicks/by-date | Get the clicks by dates
[**clicks_by_query**](StatsApi.md#clicks_by_query) | **GET** /api/v2/stats/clicks/by-query/{query} | Get the products clicked given a certain query
[**clicks_top**](StatsApi.md#clicks_top) | **GET** /api/v2/stats/clicks/top | Get the most common clicks
[**inits**](StatsApi.md#inits) | **GET** /api/v2/stats/inits | Get total sessions started
[**inits_by_date**](StatsApi.md#inits_by_date) | **GET** /api/v2/stats/inits/by-date | Get the sessions started by dates
[**metrics**](StatsApi.md#metrics) | **GET** /api/v2/stats/metrics | Get the search engines usage.
[**redirects**](StatsApi.md#redirects) | **GET** /api/v2/stats/redirects | Get the total amount of redirects done
[**searches**](StatsApi.md#searches) | **GET** /api/v2/stats/searches | Get total searches
[**searches_by_click**](StatsApi.md#searches_by_click) | **GET** /api/v2/stats/clicks/{dfid}/searches/top | Get the top searches that got a product clicked
[**searches_by_date**](StatsApi.md#searches_by_date) | **GET** /api/v2/stats/searches/by-date | Get the searches by dates
[**searches_top**](StatsApi.md#searches_top) | **GET** /api/v2/stats/searches/top | Get the most common searches
[**usage**](StatsApi.md#usage) | **GET** /api/v2/stats/usage | Get the search engines usage.


# **banners_clicks**
> object banners_clicks(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the total amount of clicks banners have got

Gets how many times a banner has been clicked

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the total amount of clicks banners have got
    api_response = api_instance.banners_clicks(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->banners_clicks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banners_display**
> object banners_display(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the total amount of displays banners have got

Gets how many times a banner has been shown

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the total amount of displays banners have got
    api_response = api_instance.banners_display(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->banners_display: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkouts**
> object checkouts(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)

Get total checkouts

Gets a total of the checkouts in a time period

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)

try:
    # Get total checkouts
    api_response = api_instance.checkouts(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->checkouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkouts_by_date**
> object checkouts_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)

Get the checkouts by dates

Gets a total of the checkouts aggregated in a time period, separated by dates

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)
query_name = 'query_name_example' # str | Type of query to filter by (optional)
total_hits = 56 # int | Filter by total hits (optional)
interval = '1d' # str | Time interval for aggregations (optional) (default to 1d)

try:
    # Get the checkouts by dates
    api_response = api_instance.checkouts_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->checkouts_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 
 **query_name** | **str**| Type of query to filter by | [optional] 
 **total_hits** | **int**| Filter by total hits | [optional] 
 **interval** | **str**| Time interval for aggregations | [optional] [default to 1d]

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clicks**
> object clicks(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)

Get total clicks

Gets a total of the clicks in a time period

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)

try:
    # Get total clicks
    api_response = api_instance.clicks(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->clicks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clicks_by_date**
> object clicks_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)

Get the clicks by dates

Gets a total of the clicks aggregated in a time period, separated by dates

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)
query_name = 'query_name_example' # str | Type of query to filter by (optional)
total_hits = 56 # int | Filter by total hits (optional)
interval = '1d' # str | Time interval for aggregations (optional) (default to 1d)

try:
    # Get the clicks by dates
    api_response = api_instance.clicks_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->clicks_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 
 **query_name** | **str**| Type of query to filter by | [optional] 
 **total_hits** | **int**| Filter by total hits | [optional] 
 **interval** | **str**| Time interval for aggregations | [optional] [default to 1d]

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clicks_by_query**
> object clicks_by_query(hashid, query, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the products clicked given a certain query

Get the products clicked given a certain query

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
query = 'query_example' # str | Search query term
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the products clicked given a certain query
    api_response = api_instance.clicks_by_query(hashid, query, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->clicks_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **query** | **str**| Search query term | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clicks_top**
> object clicks_top(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the most common clicks

Gets a top of the clicks in a time period

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the most common clicks
    api_response = api_instance.clicks_top(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->clicks_top: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inits**
> object inits(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)

Get total sessions started

Gets a total of the sessions started in a time period

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)

try:
    # Get total sessions started
    api_response = api_instance.inits(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->inits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inits_by_date**
> object inits_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)

Get the sessions started by dates

Gets a total of the sessions started aggregated in a time period, separated by dates

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)
query_name = 'query_name_example' # str | Type of query to filter by (optional)
total_hits = 56 # int | Filter by total hits (optional)
interval = '1d' # str | Time interval for aggregations (optional) (default to 1d)

try:
    # Get the sessions started by dates
    api_response = api_instance.inits_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->inits_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 
 **query_name** | **str**| Type of query to filter by | [optional] 
 **total_hits** | **int**| Filter by total hits | [optional] 
 **interval** | **str**| Time interval for aggregations | [optional] [default to 1d]

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> object metrics(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, interval=interval)

Get the search engines usage.

Gets the search engines usage, close to the current minute, but slow.

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
interval = '1d' # str | Time interval for aggregations (optional) (default to 1d)

try:
    # Get the search engines usage.
    api_response = api_instance.metrics(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **interval** | **str**| Time interval for aggregations | [optional] [default to 1d]

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirects**
> object redirects(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the total amount of redirects done

Gets how many times there's been a redirect

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the total amount of redirects done
    api_response = api_instance.redirects(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->redirects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches**
> object searches(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)

Get total searches

Gets a total of the searches in a time period

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)

try:
    # Get total searches
    api_response = api_instance.searches(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_by_click**
> object searches_by_click(hashid, dfid, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the top searches that got a product clicked

Gets the top searches that got a click in a product, and how many times.

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dfid = 'dfid_example' # str | Doofinder ID to filter by
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the top searches that got a product clicked
    api_response = api_instance.searches_by_click(hashid, dfid, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->searches_by_click: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dfid** | **str**| Doofinder ID to filter by | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_by_date**
> object searches_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)

Get the searches by dates

Gets a total of the searches in a time period, separated by dates

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
custom_results_id = 'custom_results_id_example' # str | Filter by custom results (optional)
query_name = 'query_name_example' # str | Type of query to filter by (optional)
total_hits = 56 # int | Filter by total hits (optional)
interval = '1d' # str | Time interval for aggregations (optional) (default to 1d)

try:
    # Get the searches by dates
    api_response = api_instance.searches_by_date(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, custom_results_id=custom_results_id, query_name=query_name, total_hits=total_hits, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->searches_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **custom_results_id** | **str**| Filter by custom results | [optional] 
 **query_name** | **str**| Type of query to filter by | [optional] 
 **total_hits** | **int**| Filter by total hits | [optional] 
 **interval** | **str**| Time interval for aggregations | [optional] [default to 1d]

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searches_top**
> object searches_top(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)

Get the most common searches

Gets a top of the searches in a time period

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)

try:
    # Get the most common searches
    api_response = api_instance.searches_top(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->searches_top: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage**
> object usage(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, interval=interval, type=type)

Get the search engines usage.

Gets the search engines usage, up until previous day, fast call.

### Example
```python
from __future__ import print_function
import time
import pydoof2
from pydoof2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof2.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof2.StatsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | HashID of the search engine to query or a list in the format [hashid1,hashid2,...]
dto = 'dto_example' # str | Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. (optional)
dfrom = 'dfrom_example' # str | Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. (optional)
tz = 'tz_example' # str | Timezone for the given dates, by default assumes UTC. (optional)
device = 'device_example' # str | Device filter, by default is all (optional)
interval = '1d' # str | Time interval for aggregations (optional) (default to 1d)
type = 'type_example' # str | Filter by the given usage type. (optional)

try:
    # Get the search engines usage.
    api_response = api_instance.usage(hashid, dto=dto, dfrom=dfrom, tz=tz, device=device, interval=interval, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| HashID of the search engine to query or a list in the format [hashid1,hashid2,...] | 
 **dto** | **str**| Date end of the interval in the format of UNIX timestamp or YYYYMMDD. Today, by default. | [optional] 
 **dfrom** | **str**| Date start of the interval in the format of UNIX timestamp or YYYYMMDD. By default, 10 days from current date. | [optional] 
 **tz** | **str**| Timezone for the given dates, by default assumes UTC. | [optional] 
 **device** | **str**| Device filter, by default is all | [optional] 
 **interval** | **str**| Time interval for aggregations | [optional] [default to 1d]
 **type** | **str**| Filter by the given usage type. | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

