# pydoof2.TasksApi

All URIs are relative to *https://eu1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process**](TasksApi.md#process) | **POST** /api/v2/search_engines/{hashid}/_process | Process Search Engine Data Sources
[**process_status**](TasksApi.md#process_status) | **GET** /api/v2/search_engines/{hashid}/_process | 


# **process**
> object process(hashid, datatypes=datatypes)

Process Search Engine Data Sources

Schedule a task for process data sources

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
api_instance = pydoof2.TasksApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
datatypes = 'datatypes_example' # str | List of datatypes to be processed (optional). (optional)

try:
    # Process Search Engine Data Sources
    api_response = api_instance.process(hashid, datatypes=datatypes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **datatypes** | **str**| List of datatypes to be processed (optional). | [optional] 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_status**
> object process_status(hashid)





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
api_instance = pydoof2.TasksApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)

try:
    # 
    api_response = api_instance.process_status(hashid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->process_status: %s\n" % e)
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

