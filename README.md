# PyDoof2
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 3.0.2
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://doofinder.com/support](https://doofinder.com/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import pydoof2 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pydoof2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://eu1-api.doofinder.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataTypesApi* | [**datatype_create**](docs/DataTypesApi.md#datatype_create) | **POST** /api/v2/search_engines/{hashid}/datatypes | Create a datatype
*DataTypesApi* | [**datatype_delete**](docs/DataTypesApi.md#datatype_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name} | Delete a datatype
*DataTypesApi* | [**datatype_index**](docs/DataTypesApi.md#datatype_index) | **GET** /api/v2/search_engines/{hashid}/datatypes | List datatypes
*DataTypesApi* | [**datatype_show**](docs/DataTypesApi.md#datatype_show) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name} | Get a datatype
*DataTypesApi* | [**datatype_update**](docs/DataTypesApi.md#datatype_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name} | Update a datatype
*ItemsApi* | [**item_create**](docs/ItemsApi.md#item_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/items/ | Creates an item.
*ItemsApi* | [**item_delete**](docs/ItemsApi.md#item_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/items/{item_id} | Deletes an item.
*ItemsApi* | [**item_index**](docs/ItemsApi.md#item_index) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/items/ | Scrolls through all items
*ItemsApi* | [**item_show**](docs/ItemsApi.md#item_show) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/items/{item_id} | Get an item
*ItemsApi* | [**item_temp_create**](docs/ItemsApi.md#item_temp_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/ | Creates an item in the temporal datatype
*ItemsApi* | [**item_temp_delete**](docs/ItemsApi.md#item_temp_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/{item_id} | Deletes an item in the temporal datatype
*ItemsApi* | [**item_temp_show**](docs/ItemsApi.md#item_temp_show) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/{item_id} | Get an item from the temporal datatype
*ItemsApi* | [**item_temp_update**](docs/ItemsApi.md#item_temp_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/{item_id} | Partially updates an item in the temporal datatype
*ItemsApi* | [**item_update**](docs/ItemsApi.md#item_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/items/{item_id} | Partially updates an item.
*ItemsApi* | [**items_bulk_create**](docs/ItemsApi.md#items_bulk_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/items/_bulk | Creates items in bulk
*ItemsApi* | [**items_bulk_delete**](docs/ItemsApi.md#items_bulk_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/items/_bulk | Deletes items in bulk
*ItemsApi* | [**items_bulk_update**](docs/ItemsApi.md#items_bulk_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/items/_bulk | Partial updates items in bulk
*ItemsApi* | [**items_temp_bulk_create**](docs/ItemsApi.md#items_temp_bulk_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/_bulk | Creates items in bulk in the temporal datatype
*ItemsApi* | [**items_temp_bulk_delete**](docs/ItemsApi.md#items_temp_bulk_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/_bulk | Deletes items in bulk in the temporal datatype
*ItemsApi* | [**items_temp_bulk_update**](docs/ItemsApi.md#items_temp_bulk_update) | **PATCH** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/items/_bulk | Partial updates items in bulk in the temporal datatype
*SearchEnginesApi* | [**search_engine_create**](docs/SearchEnginesApi.md#search_engine_create) | **POST** /api/v2/search_engines | Create new search engine 
*SearchEnginesApi* | [**search_engine_delete**](docs/SearchEnginesApi.md#search_engine_delete) | **DELETE** /api/v2/search_engines/{hashid} | Delete a search engine
*SearchEnginesApi* | [**search_engine_list**](docs/SearchEnginesApi.md#search_engine_list) | **GET** /api/v2/search_engines | List search engines
*SearchEnginesApi* | [**search_engine_show**](docs/SearchEnginesApi.md#search_engine_show) | **GET** /api/v2/search_engines/{hashid} | Get a search engine
*SearchEnginesApi* | [**search_engine_update**](docs/SearchEnginesApi.md#search_engine_update) | **PATCH** /api/v2/search_engines/{hashid} | Update a search engine
*StatsApi* | [**banners_clicks**](docs/StatsApi.md#banners_clicks) | **GET** /api/v2/stats/banners/clicks | Get the total amount of clicks banners have got
*StatsApi* | [**banners_display**](docs/StatsApi.md#banners_display) | **GET** /api/v2/stats/banners/display | Get the total amount of displays banners have got
*StatsApi* | [**checkouts**](docs/StatsApi.md#checkouts) | **GET** /api/v2/stats/checkouts | Get total checkouts
*StatsApi* | [**checkouts_by_date**](docs/StatsApi.md#checkouts_by_date) | **GET** /api/v2/stats/checkouts/by-date | Get the checkouts by dates
*StatsApi* | [**clicks**](docs/StatsApi.md#clicks) | **GET** /api/v2/stats/clicks | Get total clicks
*StatsApi* | [**clicks_by_date**](docs/StatsApi.md#clicks_by_date) | **GET** /api/v2/stats/clicks/by-date | Get the clicks by dates
*StatsApi* | [**clicks_by_query**](docs/StatsApi.md#clicks_by_query) | **GET** /api/v2/stats/clicks/by-query/{query} | Get the products clicked given a certain query
*StatsApi* | [**clicks_top**](docs/StatsApi.md#clicks_top) | **GET** /api/v2/stats/clicks/top | Get the most common clicks
*StatsApi* | [**inits**](docs/StatsApi.md#inits) | **GET** /api/v2/stats/inits | Get total sessions started
*StatsApi* | [**inits_by_date**](docs/StatsApi.md#inits_by_date) | **GET** /api/v2/stats/inits/by-date | Get the sessions started by dates
*StatsApi* | [**metrics**](docs/StatsApi.md#metrics) | **GET** /api/v2/stats/metrics | Get the search engines usage.
*StatsApi* | [**redirects**](docs/StatsApi.md#redirects) | **GET** /api/v2/stats/redirects | Get the total amount of redirects done
*StatsApi* | [**searches**](docs/StatsApi.md#searches) | **GET** /api/v2/stats/searches | Get total searches
*StatsApi* | [**searches_by_click**](docs/StatsApi.md#searches_by_click) | **GET** /api/v2/stats/clicks/{dfid}/searches/top | Get the top searches that got a product clicked
*StatsApi* | [**searches_by_date**](docs/StatsApi.md#searches_by_date) | **GET** /api/v2/stats/searches/by-date | Get the searches by dates
*StatsApi* | [**searches_top**](docs/StatsApi.md#searches_top) | **GET** /api/v2/stats/searches/top | Get the most common searches
*StatsApi* | [**usage**](docs/StatsApi.md#usage) | **GET** /api/v2/stats/usage | Get the search engines usage.
*TasksApi* | [**process**](docs/TasksApi.md#process) | **POST** /api/v2/search_engines/{hashid}/_process | Process Search Engine Data Sources
*TasksApi* | [**process_status**](docs/TasksApi.md#process_status) | **GET** /api/v2/search_engines/{hashid}/_process | 
*TemporaryIndicesApi* | [**get_reindexing_status**](docs/TemporaryIndicesApi.md#get_reindexing_status) | **GET** /api/v2/search_engines/{hashid}/datatypes/{name}/_reindex_to_temp/ | Return the status of the current reindexing task.
*TemporaryIndicesApi* | [**reindex_to_temp**](docs/TemporaryIndicesApi.md#reindex_to_temp) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/_reindex_to_temp/ | Reindex the content of the real index into the temporary one.
*TemporaryIndicesApi* | [**replace_by_temp**](docs/TemporaryIndicesApi.md#replace_by_temp) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/_replace_by_temp/ | Replace the real index with the temporary one.
*TemporaryIndicesApi* | [**temporary_index_create**](docs/TemporaryIndicesApi.md#temporary_index_create) | **POST** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/ | Creates a temporary index
*TemporaryIndicesApi* | [**temporary_index_delete**](docs/TemporaryIndicesApi.md#temporary_index_delete) | **DELETE** /api/v2/search_engines/{hashid}/datatypes/{name}/temp/ | Deletes the temporary index.


## Documentation For Models

 - [BulkOperation](docs/BulkOperation.md)
 - [BulkResult](docs/BulkResult.md)
 - [BulkResultResults](docs/BulkResultResults.md)
 - [DataSources](docs/DataSources.md)
 - [DataTypes](docs/DataTypes.md)
 - [Item](docs/Item.md)
 - [Items](docs/Items.md)
 - [NewSearchEngine](docs/NewSearchEngine.md)
 - [Scroll](docs/Scroll.md)
 - [SearchEngines](docs/SearchEngines.md)
 - [UpdateDataSource](docs/UpdateDataSource.md)
 - [UpdateDataType](docs/UpdateDataType.md)
 - [DataSource](docs/DataSource.md)
 - [DataType](docs/DataType.md)
 - [SearchEngine](docs/SearchEngine.md)


## Documentation For Authorization


## api_token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## jwt_token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@doofinder.com

