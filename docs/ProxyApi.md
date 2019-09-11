# pydoof.ProxyApi

All URIs are relative to *https://us1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logs**](ProxyApi.md#logs) | **GET** /api/v2/search_engines/{hashid}/logs | List tasks logs
[**task_details**](ProxyApi.md#task_details) | **GET** /api/v2/search_engines/{hashid}/tasks/{task_id} | Get Task details
[**tasks_process**](ProxyApi.md#tasks_process) | **POST** /api/v2/search_engines/{hashid}/tasks/process | Process Search Engine Data Sources


# **logs**
> object logs(hashid)

List tasks logs

List tasks detail logs

### Example
```python
from __future__ import print_function
import time
import pydoof
from pydoof.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof.ProxyApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)

try:
    # List tasks logs
    api_response = api_instance.logs(hashid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->logs: %s\n" % e)
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

# **task_details**
> object task_details(hashid, task_id)

Get Task details

Show the details of a given task.

### Example
```python
from __future__ import print_function
import time
import pydoof
from pydoof.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof.ProxyApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
task_id = 'task_id_example' # str | Id of the task

try:
    # Get Task details
    api_response = api_instance.task_details(hashid, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->task_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **task_id** | **str**| Id of the task | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_process**
> object tasks_process(hashid)

Process Search Engine Data Sources

Schedule a task for process data sources

### Example
```python
from __future__ import print_function
import time
import pydoof
from pydoof.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = pydoof.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: jwt_token
configuration = pydoof.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pydoof.ProxyApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)

try:
    # Process Search Engine Data Sources
    api_response = api_instance.tasks_process(hashid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProxyApi->tasks_process: %s\n" % e)
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

