# pydoof.HealthApi

All URIs are relative to *https://us1-api.doofinder.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status**](HealthApi.md#status) | **GET** /status | Load balancer check


# **status**
> object status()

Load balancer check

Allows detection of failures.

### Example
```python
from __future__ import print_function
import time
import pydoof
from pydoof.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pydoof.HealthApi()

try:
    # Load balancer check
    api_response = api_instance.status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: plain/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

