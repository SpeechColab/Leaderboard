# TranscriptionProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diarization_enabled** | **bool** | A value indicating whether diarization (speaker identification) is requested. The default value  is &#x60;false&#x60;.  If this field is set to true and the improved diarization system is configured by specifying  &#x60;DiarizationProperties&#x60;, the improved diarization system will provide diarization for a configurable  range of speakers.  If this field is set to true and the improved diarization system is not enabled (not specifying  &#x60;DiarizationProperties&#x60;), the basic diarization system will distinguish between up to two speakers.  No extra charges are applied for the basic diarization.                The basic diarization system is deprecated and will be removed in the next major version of the API.  This &#x60;diarizationEnabled&#x60; setting will also be removed. | [optional] 
**word_level_timestamps_enabled** | **bool** | A value indicating whether word level timestamps are requested. The default value is  &#x60;false&#x60;. | [optional] 
**display_form_word_level_timestamps_enabled** | **bool** | A value indicating whether word level timestamps for the display form are requested. The default value is &#x60;false&#x60;. | [optional] 
**duration** | **str** | The duration of the transcription. The duration is encoded as ISO 8601 duration  (\&quot;PnYnMnDTnHnMnS\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Durations). | [optional] 
**channels** | **list[int]** | A collection of the requested channel numbers.  In the default case, the channels 0 and 1 are considered. | [optional] 
**destination_container_url** | **str** | The requested destination container.  ### Remarks ###  When a destination container is used in combination with a &#x60;timeToLive&#x60;, the metadata of a  transcription will be deleted normally, but the data stored in the destination container, including  transcription results, will remain untouched, because no delete permissions are required for this  container.&lt;br /&gt;  To support automatic cleanup, either configure blob lifetimes on the container, or use \&quot;Bring your own Storage (BYOS)\&quot;  instead of &#x60;destinationContainerUrl&#x60;, where blobs can be cleaned up. | [optional] 
**punctuation_mode** | [**PunctuationMode**](PunctuationMode.md) |  | [optional] 
**profanity_filter_mode** | [**ProfanityFilterMode**](ProfanityFilterMode.md) |  | [optional] 
**time_to_live** | **str** | How long the transcription will be kept in the system after it has completed. Once the  transcription reaches the time to live after completion (successful or failed) it will be automatically  deleted. Not setting this value or setting it to 0 will disable automatic deletion. The longest supported  duration is 31 days.  The duration is encoded as ISO 8601 duration (\&quot;PnYnMnDTnHnMnS\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Durations). | [optional] 
**diarization** | [**DiarizationProperties**](DiarizationProperties.md) |  | [optional] 
**language_identification** | [**LanguageIdentificationProperties**](LanguageIdentificationProperties.md) |  | [optional] 
**email** | **str** | The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email. | [optional] 
**error** | [**EntityError**](EntityError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


