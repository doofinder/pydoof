# SearchEngine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stopwords** | **bool** | Ignore high-frequency terms like \&quot;the\&quot;, \&quot;and\&quot;, \&quot;is\&quot;. These words have a low weight and contribute little to the relevance score. | [optional] 
**site_url** | **str** | The url of the site for the search engine | [optional] 
**name** | **str** | A verbose name that helps to describe the search engine | 
**language** | **str** | An ISO 639-1 language code that determines the language of the search engine. E.g.: ‘es’. | 
**inactive** | **bool** | Indicates if the search engine has been deactivated and therefore it can not receive requests (read-only) | [optional] 
**hashid** | **str** | A unique code that identify a search engine (read-only) | [optional] 
**datatypes** | [**DataTypes**](DataTypes.md) | List of datatypes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


