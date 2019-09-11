# pydoof2.DataTypesApi

All URIs are relative to *https://us1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datatype_create**](DataTypesApi.md#datatype_create) | **POST** /api/v2/search_engines/{hashid}/datatypes | Create a datatype
[**datatype_delete**](DataTypesApi.md#datatype_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name} | Delete a datatype
[**datatype_index**](DataTypesApi.md#datatype_index) | **GET** /api/v2/search_engines/{hashid}/datatypes | List datatypes
[**datatype_show**](DataTypesApi.md#datatype_show) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name} | Get a datatype
[**datatype_update**](DataTypesApi.md#datatype_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name} | Update a datatype


# **datatype_create**
> DataType datatype_create(hashid, datatype)

Create a datatype

Create new datatype for the given search engine

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
api_instance = pydoof2.DataTypesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
datatype = pydoof2.DataType() # DataType | DataType data

try:
    # Create a datatype
    api_response = api_instance.datatype_create(hashid, datatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->datatype_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **datatype** | [**DataType**](DataType.md)| DataType data | 

### Return type

[**DataType**](DataType.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datatype_delete**
> object datatype_delete(hashid, name)

Delete a datatype

Delete a datatype for the given search engine and name

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
api_instance = pydoof2.DataTypesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype

try:
    # Delete a datatype
    api_response = api_instance.datatype_delete(hashid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->datatype_delete: %s\n" % e)
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

# **datatype_index**
> DataTypes datatype_index(hashid)

List datatypes

List the datatypes of the given search engine

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
api_instance = pydoof2.DataTypesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)

try:
    # List datatypes
    api_response = api_instance.datatype_index(hashid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->datatype_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 

### Return type

[**DataTypes**](DataTypes.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datatype_show**
> DataType datatype_show(hashid, name)

Get a datatype

Get datatype of the given search engine and name

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
api_instance = pydoof2.DataTypesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype

try:
    # Get a datatype
    api_response = api_instance.datatype_show(hashid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->datatype_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 

### Return type

[**DataType**](DataType.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datatype_update**
> DataType datatype_update(hashid, name, datatype)

Update a datatype

Update a datatype for the given search engine and name

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
api_instance = pydoof2.DataTypesApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
datatype = pydoof2.UpdateDataType() # UpdateDataType | DataType data

try:
    # Update a datatype
    api_response = api_instance.datatype_update(hashid, name, datatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->datatype_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **datatype** | [**UpdateDataType**](UpdateDataType.md)| DataType data | 

### Return type

[**DataType**](DataType.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

