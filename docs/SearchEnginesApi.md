# pydoof2.SearchEnginesApi

All URIs are relative to *https://eu1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_engine_create**](SearchEnginesApi.md#search_engine_create) | **POST** /api/v2/search_engines | Create new search engine 
[**search_engine_delete**](SearchEnginesApi.md#search_engine_delete) | **DELETE** /api/v2/search_engines/{hashid} | Delete a search engine
[**search_engine_list**](SearchEnginesApi.md#search_engine_list) | **GET** /api/v2/search_engines | List search engines
[**search_engine_show**](SearchEnginesApi.md#search_engine_show) | **GET** /api/v2/search_engines/{hashid} | Get a search engine
[**search_engine_update**](SearchEnginesApi.md#search_engine_update) | **PATCH** /api/v2/search_engines/{hashid} | Update a search engine


# **search_engine_create**
> SearchEngine search_engine_create(searchengine)

Create new search engine 

Create a new search engine

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
api_instance = pydoof2.SearchEnginesApi(pydoof2.ApiClient(configuration))
searchengine = pydoof2.NewSearchEngine() # NewSearchEngine | Search engine data

try:
    # Create new search engine 
    api_response = api_instance.search_engine_create(searchengine)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchEnginesApi->search_engine_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchengine** | [**NewSearchEngine**](NewSearchEngine.md)| Search engine data | 

### Return type

[**SearchEngine**](SearchEngine.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_engine_delete**
> object search_engine_delete(hashid)

Delete a search engine

Delete a search engine

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
api_instance = pydoof2.SearchEnginesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)

try:
    # Delete a search engine
    api_response = api_instance.search_engine_delete(hashid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchEnginesApi->search_engine_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_engine_list**
> SearchEngines search_engine_list()

List search engines

List search engines

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
api_instance = pydoof2.SearchEnginesApi(pydoof2.ApiClient(configuration))

try:
    # List search engines
    api_response = api_instance.search_engine_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchEnginesApi->search_engine_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchEngines**](SearchEngines.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_engine_show**
> SearchEngine search_engine_show(hashid)

Get a search engine

Get a search engine given by his hashid

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
api_instance = pydoof2.SearchEnginesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)

try:
    # Get a search engine
    api_response = api_instance.search_engine_show(hashid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchEnginesApi->search_engine_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 

### Return type

[**SearchEngine**](SearchEngine.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_engine_update**
> SearchEngine search_engine_update(hashid, searchengine)

Update a search engine

Update a search engine by the given hashid

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
api_instance = pydoof2.SearchEnginesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
searchengine = pydoof2.NewSearchEngine() # NewSearchEngine | Search engine data

try:
    # Update a search engine
    api_response = api_instance.search_engine_update(hashid, searchengine)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchEnginesApi->search_engine_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **searchengine** | [**NewSearchEngine**](NewSearchEngine.md)| Search engine data | 

### Return type

[**SearchEngine**](SearchEngine.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

