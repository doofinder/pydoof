# pydoof.TempIndicesApi

All URIs are relative to *https://us1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reindex_to_temp**](TempIndicesApi.md#reindex_to_temp) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/reindex_to_temp/ | Reindex the content of the real index into the temporary one.
[**replace_by_temp**](TempIndicesApi.md#replace_by_temp) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/replace_by_temp/ | Replace the real index with the temporary one.
[**temporary_index_create**](TempIndicesApi.md#temporary_index_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/ | Creates a temporary index
[**temporary_index_delete**](TempIndicesApi.md#temporary_index_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/ | Deletes the temporary index.


# **reindex_to_temp**
> object reindex_to_temp(hashid, name)

Reindex the content of the real index into the temporary one.

This executes a reindexing operation between the real index and the temporary one, taking all items from real and creating them in the temporary. This will return a 404 (Not found) if there is no temporary index. 

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
api_instance = pydoof.TempIndicesApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype

try:
    # Reindex the content of the real index into the temporary one.
    api_response = api_instance.reindex_to_temp(hashid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TempIndicesApi->reindex_to_temp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_by_temp**
> object replace_by_temp(hashid, name)

Replace the real index with the temporary one.

This request takes the temporary index and \"overwrites\" the real one. Any content in the real index will be lost with this operation. 

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
api_instance = pydoof.TempIndicesApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype

try:
    # Replace the real index with the temporary one.
    api_response = api_instance.replace_by_temp(hashid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TempIndicesApi->replace_by_temp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporary_index_create**
> object temporary_index_create(hashid, name)

Creates a temporary index

Creates a new temporary index for the given datatype. There could not be two temporary index at the same time so any request made to this endpoint when there is one created will fail. Creating a temporary index also set a lock preventing any changes on the search engine. 

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
api_instance = pydoof.TempIndicesApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype

try:
    # Creates a temporary index
    api_response = api_instance.temporary_index_create(hashid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TempIndicesApi->temporary_index_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporary_index_delete**
> object temporary_index_delete(hashid, name)

Deletes the temporary index.

Deletes the temporary index. This also removes the lock in the search engine. If there is no temporary index this will return a 404 (Not found). 

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
api_instance = pydoof.TempIndicesApi(pydoof.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype

try:
    # Deletes the temporary index.
    api_response = api_instance.temporary_index_delete(hashid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TempIndicesApi->temporary_index_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

