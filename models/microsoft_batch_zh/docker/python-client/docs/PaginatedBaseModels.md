# PaginatedBaseModels

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**list[BaseModel]**](BaseModel.md) | A list of entities limited by either the passed query parameters &#39;skip&#39; and &#39;top&#39; or their default values.                When iterating through a list using pagination and deleting entities in parallel, some entities will be skipped in the results.  It&#39;s recommended to build a list on the client and delete after the fetching of the complete list. | [optional] 
**next_link** | **str** | A link to the next set of paginated results if there are more entities available; otherwise null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


