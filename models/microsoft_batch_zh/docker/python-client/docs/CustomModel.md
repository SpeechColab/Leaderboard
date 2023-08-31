# CustomModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**EntityReference**](EntityReference.md) |  | [optional] 
**links** | [**CustomModelLinks**](CustomModelLinks.md) |  | [optional] 
**properties** | [**CustomModelProperties**](CustomModelProperties.md) |  | [optional] 
**text** | **str** | The text used to adapt this language model. | [optional] 
**base_model** | [**EntityReference**](EntityReference.md) |  | [optional] 
**datasets** | [**list[EntityReference]**](EntityReference.md) | Datasets used for adaptation. | [optional] 
**custom_properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


