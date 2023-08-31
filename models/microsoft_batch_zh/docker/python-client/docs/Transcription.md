# Transcription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**TranscriptionLinks**](TranscriptionLinks.md) |  | [optional] 
**properties** | [**TranscriptionProperties**](TranscriptionProperties.md) |  | [optional] 
**_self** | **str** | The location of this entity. | [optional] 
**model** | [**EntityReference**](EntityReference.md) |  | [optional] 
**project** | [**EntityReference**](EntityReference.md) |  | [optional] 
**dataset** | [**EntityReference**](EntityReference.md) |  | [optional] 
**content_urls** | **list[str]** | A list of content urls to get audio files to transcribe. Up to 1000 urls are allowed.  This property will not be returned in a response. | [optional] 
**content_container_url** | **str** | A URL for an Azure blob container that contains the audio files. A container is allowed to have a maximum size of 5GB and a maximum number of 10000 blobs.  The maximum size for a blob is 2.5GB.  Container SAS should contain &#39;r&#39; (read) and &#39;l&#39; (list) permissions.  This property will not be returned in a response. | [optional] 
**locale** | **str** | The locale of the contained data. If Language Identification is used, this locale is used to transcribe speech for which no language could be detected. | 
**display_name** | **str** | The display name of the object. | 
**description** | **str** | The description of the object. | [optional] 
**custom_properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


