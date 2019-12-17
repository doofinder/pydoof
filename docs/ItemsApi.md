# pydoof2.ItemsApi

All URIs are relative to *https://eu1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**item_create**](ItemsApi.md#item_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/items/ | Creates an item.
[**item_delete**](ItemsApi.md#item_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/items/{item_id} | Deletes an item.
[**item_index**](ItemsApi.md#item_index) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/items/ | Scrolls through all items
[**item_show**](ItemsApi.md#item_show) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/items/{item_id} | Get an item
[**item_temp_create**](ItemsApi.md#item_temp_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/ | Creates an item in the temporal datatype
[**item_temp_delete**](ItemsApi.md#item_temp_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/{item_id} | Deletes an item in the temporal datatype
[**item_temp_show**](ItemsApi.md#item_temp_show) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/{item_id} | Get an item from the temporal datatype
[**item_temp_update**](ItemsApi.md#item_temp_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/{item_id} | Partially updates an item in the temporal datatype
[**item_update**](ItemsApi.md#item_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/items/{item_id} | Partially updates an item.
[**items_bulk_create**](ItemsApi.md#items_bulk_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/items/_bulk | Creates items in bulk
[**items_bulk_delete**](ItemsApi.md#items_bulk_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/items/_bulk | Deletes items in bulk
[**items_bulk_update**](ItemsApi.md#items_bulk_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/items/_bulk | Partial updates items in bulk
[**items_temp_bulk_create**](ItemsApi.md#items_temp_bulk_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/_bulk | Creates items in bulk in the temporal datatype
[**items_temp_bulk_delete**](ItemsApi.md#items_temp_bulk_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/_bulk | Deletes items in bulk in the temporal datatype
[**items_temp_bulk_update**](ItemsApi.md#items_temp_bulk_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/_bulk | Partial updates items in bulk in the temporal datatype


# **item_create**
> Item item_create(hashid, name, item)

Creates an item.

Creates an item with the data provided.

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item = pydoof2.Item() # Item | Item fields

try:
    # Creates an item.
    api_response = api_instance.item_create(hashid, name, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item** | [**Item**](Item.md)| Item fields | 

### Return type

[**Item**](Item.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_delete**
> object item_delete(hashid, name, item_id)

Deletes an item.

Deletes an item given its id.

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item_id = 'item_id_example' # str | Item unique identifier

try:
    # Deletes an item.
    api_response = api_instance.item_delete(hashid, name, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item_id** | **str**| Item unique identifier | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_index**
> Scroll item_index(hashid, name, scroll_id=scroll_id, rpp=rpp)

Scrolls through all items

Starts a scroll through all items. Generate a scroll id that can be traversed with successive requests.

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
scroll_id = 'scroll_id_example' # str | Unique identifier for the scroll. The scroll saves a \"pointer\" to the last fetched page. (optional)
rpp = 56 # int | _Results per page_. How many items are fetched per page (optional)

try:
    # Scrolls through all items
    api_response = api_instance.item_index(hashid, name, scroll_id=scroll_id, rpp=rpp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **scroll_id** | **str**| Unique identifier for the scroll. The scroll saves a \&quot;pointer\&quot; to the last fetched page. | [optional] 
 **rpp** | **int**| _Results per page_. How many items are fetched per page | [optional] 

### Return type

[**Scroll**](Scroll.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_show**
> Item item_show(hashid, name, item_id)

Get an item

Fetch an item from the search engine and datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item_id = 'item_id_example' # str | Item unique identifier

try:
    # Get an item
    api_response = api_instance.item_show(hashid, name, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item_id** | **str**| Item unique identifier | 

### Return type

[**Item**](Item.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_temp_create**
> Item item_temp_create(hashid, name, item)

Creates an item in the temporal datatype

Creates an item with the data provided in the temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item = pydoof2.Item() # Item | Item fields

try:
    # Creates an item in the temporal datatype
    api_response = api_instance.item_temp_create(hashid, name, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_temp_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item** | [**Item**](Item.md)| Item fields | 

### Return type

[**Item**](Item.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_temp_delete**
> object item_temp_delete(hashid, name, item_id)

Deletes an item in the temporal datatype

Deletes an item given its id in the temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item_id = 'item_id_example' # str | Item unique identifier

try:
    # Deletes an item in the temporal datatype
    api_response = api_instance.item_temp_delete(hashid, name, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_temp_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item_id** | **str**| Item unique identifier | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_temp_show**
> Item item_temp_show(hashid, name, item_id)

Get an item from the temporal datatype

Fetch an item from the search engine and temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item_id = 'item_id_example' # str | Item unique identifier

try:
    # Get an item from the temporal datatype
    api_response = api_instance.item_temp_show(hashid, name, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_temp_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item_id** | **str**| Item unique identifier | 

### Return type

[**Item**](Item.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_temp_update**
> Item item_temp_update(hashid, name, item_id, item)

Partially updates an item in the temporal datatype

Partially updates an item and returns the indexed result in the temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item_id = 'item_id_example' # str | Item unique identifier
item = pydoof2.Item() # Item | Item fields

try:
    # Partially updates an item in the temporal datatype
    api_response = api_instance.item_temp_update(hashid, name, item_id, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_temp_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item_id** | **str**| Item unique identifier | 
 **item** | [**Item**](Item.md)| Item fields | 

### Return type

[**Item**](Item.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_update**
> Item item_update(hashid, name, item_id, item)

Partially updates an item.

Partially updates an item and returns the indexed result.

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
item_id = 'item_id_example' # str | Item unique identifier
item = pydoof2.Item() # Item | Item fields

try:
    # Partially updates an item.
    api_response = api_instance.item_update(hashid, name, item_id, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->item_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **item_id** | **str**| Item unique identifier | 
 **item** | [**Item**](Item.md)| Item fields | 

### Return type

[**Item**](Item.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_bulk_create**
> BulkResult items_bulk_create(hashid, name, bulk)

Creates items in bulk

Creates an array of items in a single bulk operation

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
bulk = pydoof2.BulkOperation() # BulkOperation | Bulk data

try:
    # Creates items in bulk
    api_response = api_instance.items_bulk_create(hashid, name, bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_bulk_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **bulk** | [**BulkOperation**](BulkOperation.md)| Bulk data | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_bulk_delete**
> BulkResult items_bulk_delete(hashid, name, bulk)

Deletes items in bulk

Deletes an array of items in a single bulk operation

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
bulk = pydoof2.BulkOperation() # BulkOperation | Bulk data

try:
    # Deletes items in bulk
    api_response = api_instance.items_bulk_delete(hashid, name, bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **bulk** | [**BulkOperation**](BulkOperation.md)| Bulk data | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_bulk_update**
> BulkResult items_bulk_update(hashid, name, bulk)

Partial updates items in bulk

Updates an array of items in a single bulk operation

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
bulk = pydoof2.BulkOperation() # BulkOperation | Bulk data

try:
    # Partial updates items in bulk
    api_response = api_instance.items_bulk_update(hashid, name, bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_bulk_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **bulk** | [**BulkOperation**](BulkOperation.md)| Bulk data | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_temp_bulk_create**
> BulkResult items_temp_bulk_create(hashid, name, bulk)

Creates items in bulk in the temporal datatype

Creates an array of items in a single bulk operation in the temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
bulk = pydoof2.BulkOperation() # BulkOperation | Bulk data

try:
    # Creates items in bulk in the temporal datatype
    api_response = api_instance.items_temp_bulk_create(hashid, name, bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_temp_bulk_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **bulk** | [**BulkOperation**](BulkOperation.md)| Bulk data | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_temp_bulk_delete**
> BulkResult items_temp_bulk_delete(hashid, name, bulk)

Deletes items in bulk in the temporal datatype

Deletes an array of items in a single bulk operation in the temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
bulk = pydoof2.BulkOperation() # BulkOperation | Bulk data

try:
    # Deletes items in bulk in the temporal datatype
    api_response = api_instance.items_temp_bulk_delete(hashid, name, bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_temp_bulk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **bulk** | [**BulkOperation**](BulkOperation.md)| Bulk data | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_temp_bulk_update**
> BulkResult items_temp_bulk_update(hashid, name, bulk)

Partial updates items in bulk in the temporal datatype

Updates an array of items in a single bulk operation in the temporal datatype

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
api_instance = pydoof2.ItemsApi(pydoof2.ApiClient(configuration))
hashid = 'hashid_example' # str | Search engine identifier (hashid)
name = 'name_example' # str | Name of the datatype
bulk = pydoof2.BulkOperation() # BulkOperation | Bulk data

try:
    # Partial updates items in bulk in the temporal datatype
    api_response = api_instance.items_temp_bulk_update(hashid, name, bulk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_temp_bulk_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashid** | **str**| Search engine identifier (hashid) | 
 **name** | **str**| Name of the datatype | 
 **bulk** | [**BulkOperation**](BulkOperation.md)| Bulk data | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[api_token](../README.md#api_token), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

