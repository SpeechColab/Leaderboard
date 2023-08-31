# swagger_client.CustomSpeechEndpointsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_create**](CustomSpeechEndpointsApi.md#endpoints_create) | **POST** /endpoints | Creates a new endpoint.
[**endpoints_delete**](CustomSpeechEndpointsApi.md#endpoints_delete) | **DELETE** /endpoints/{id} | Deletes the endpoint identified by the given ID.
[**endpoints_delete_base_model_log**](CustomSpeechEndpointsApi.md#endpoints_delete_base_model_log) | **DELETE** /endpoints/base/{locale}/files/logs/{logId} | Deletes one audio or transcription log that have been stored when using the default base model of a given language.
[**endpoints_delete_base_model_logs**](CustomSpeechEndpointsApi.md#endpoints_delete_base_model_logs) | **DELETE** /endpoints/base/{locale}/files/logs | Deletes the specified audio and transcription logs that have been stored when using the default base model of a given language. It deletes all logs before (and including) a specific day.
[**endpoints_delete_log**](CustomSpeechEndpointsApi.md#endpoints_delete_log) | **DELETE** /endpoints/{id}/files/logs/{logId} | Deletes one audio or transcription log that have been stored for a given endpoint.
[**endpoints_delete_logs**](CustomSpeechEndpointsApi.md#endpoints_delete_logs) | **DELETE** /endpoints/{id}/files/logs | Deletes the specified audio and transcription logs that have been stored for a given endpoint. It deletes all logs before (and including) a specific day.
[**endpoints_get**](CustomSpeechEndpointsApi.md#endpoints_get) | **GET** /endpoints/{id} | Gets the endpoint identified by the given ID.
[**endpoints_get_base_model_log**](CustomSpeechEndpointsApi.md#endpoints_get_base_model_log) | **GET** /endpoints/base/{locale}/files/logs/{logId} | Gets a specific audio or transcription log for the default base model in a given language.
[**endpoints_get_log**](CustomSpeechEndpointsApi.md#endpoints_get_log) | **GET** /endpoints/{id}/files/logs/{logId} | Gets a specific audio or transcription log for a given endpoint.
[**endpoints_list**](CustomSpeechEndpointsApi.md#endpoints_list) | **GET** /endpoints | Gets the list of endpoints for the authenticated subscription.
[**endpoints_list_base_model_logs**](CustomSpeechEndpointsApi.md#endpoints_list_base_model_logs) | **GET** /endpoints/base/{locale}/files/logs | Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.
[**endpoints_list_logs**](CustomSpeechEndpointsApi.md#endpoints_list_logs) | **GET** /endpoints/{id}/files/logs | Gets the list of audio and transcription logs that have been stored for a given endpoint.
[**endpoints_list_supported_locales**](CustomSpeechEndpointsApi.md#endpoints_list_supported_locales) | **GET** /endpoints/locales | Gets a list of supported locales for endpoint creations.
[**endpoints_update**](CustomSpeechEndpointsApi.md#endpoints_update) | **PATCH** /endpoints/{id} | Updates the metadata of the endpoint identified by the given ID.


# **endpoints_create**
> Endpoint endpoints_create(endpoint)

Creates a new endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint = swagger_client.Endpoint() # Endpoint | The details of the endpoint.

try:
    # Creates a new endpoint.
    api_response = api_instance.endpoints_create(endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | [**Endpoint**](Endpoint.md)| The details of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete**
> endpoints_delete(id)

Deletes the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.

try:
    # Deletes the endpoint identified by the given ID.
    api_instance.endpoints_delete(id)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_base_model_log**
> endpoints_delete_base_model_log(locale, log_id)

Deletes one audio or transcription log that have been stored when using the default base model of a given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
log_id = 'log_id_example' # str | The identifier of the log.

try:
    # Deletes one audio or transcription log that have been stored when using the default base model of a given language.
    api_instance.endpoints_delete_base_model_log(locale, log_id)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_delete_base_model_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **log_id** | **str**| The identifier of the log. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_base_model_logs**
> endpoints_delete_base_model_logs(locale, end_date=end_date)

Deletes the specified audio and transcription logs that have been stored when using the default base model of a given language. It deletes all logs before (and including) a specific day.

Deletion process is done asynchronously and can take up to one day depending on the amount of log files.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
end_date = 'end_date_example' # str | The end date of the audio logs deletion (specific day, UTC).              Expected format: \"yyyy-mm-dd\". For instance, \"2019-09-20\" results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. (optional)

try:
    # Deletes the specified audio and transcription logs that have been stored when using the default base model of a given language. It deletes all logs before (and including) a specific day.
    api_instance.endpoints_delete_base_model_logs(locale, end_date=end_date)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_delete_base_model_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **end_date** | **str**| The end date of the audio logs deletion (specific day, UTC).              Expected format: \&quot;yyyy-mm-dd\&quot;. For instance, \&quot;2019-09-20\&quot; results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_log**
> endpoints_delete_log(id, log_id)

Deletes one audio or transcription log that have been stored for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
log_id = 'log_id_example' # str | The identifier of the log.

try:
    # Deletes one audio or transcription log that have been stored for a given endpoint.
    api_instance.endpoints_delete_log(id, log_id)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_delete_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **log_id** | **str**| The identifier of the log. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete_logs**
> endpoints_delete_logs(id, end_date=end_date)

Deletes the specified audio and transcription logs that have been stored for a given endpoint. It deletes all logs before (and including) a specific day.

The deletion process is done asynchronously and can take up to one day depending on the amount of log files.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
end_date = 'end_date_example' # str | The end date of the audio logs deletion (specific day, UTC).              Expected format: \"yyyy-mm-dd\". For instance, \"2019-09-20\" results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. (optional)

try:
    # Deletes the specified audio and transcription logs that have been stored for a given endpoint. It deletes all logs before (and including) a specific day.
    api_instance.endpoints_delete_logs(id, end_date=end_date)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_delete_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **end_date** | **str**| The end date of the audio logs deletion (specific day, UTC).              Expected format: \&quot;yyyy-mm-dd\&quot;. For instance, \&quot;2019-09-20\&quot; results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get**
> Endpoint endpoints_get(id)

Gets the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.

try:
    # Gets the endpoint identified by the given ID.
    api_response = api_instance.endpoints_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get_base_model_log**
> File endpoints_get_base_model_log(locale, log_id, sas_validity_in_seconds=sas_validity_in_seconds)

Gets a specific audio or transcription log for the default base model in a given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
log_id = 'log_id_example' # str | The identifier of the log.
sas_validity_in_seconds = 56 # int | The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Gets a specific audio or transcription log for the default base model in a given language.
    api_response = api_instance.endpoints_get_base_model_log(locale, log_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_get_base_model_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **log_id** | **str**| The identifier of the log. | 
 **sas_validity_in_seconds** | **int**| The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_get_log**
> File endpoints_get_log(id, log_id, sas_validity_in_seconds=sas_validity_in_seconds)

Gets a specific audio or transcription log for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
log_id = 'log_id_example' # str | The identifier of the log.
sas_validity_in_seconds = 56 # int | The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Gets a specific audio or transcription log for a given endpoint.
    api_response = api_instance.endpoints_get_log(id, log_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_get_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **log_id** | **str**| The identifier of the log. | 
 **sas_validity_in_seconds** | **int**| The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list**
> PaginatedEndpoints endpoints_list(skip=skip, top=top, filter=filter)

Gets the list of endpoints for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available endpoints.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=locale eq 'en-US' (optional)

try:
    # Gets the list of endpoints for the authenticated subscription.
    api_response = api_instance.endpoints_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available endpoints.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;locale eq &#39;en-US&#39; | [optional] 

### Return type

[**PaginatedEndpoints**](PaginatedEndpoints.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_base_model_logs**
> PaginatedFiles endpoints_list_base_model_logs(locale, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)

Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
sas_validity_in_seconds = 56 # int | The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip_token = 'skip_token_example' # str | Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)

try:
    # Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.
    api_response = api_instance.endpoints_list_base_model_logs(locale, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_list_base_model_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **sas_validity_in_seconds** | **int**| The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip_token** | **str**| Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_logs**
> PaginatedFiles endpoints_list_logs(id, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)

Gets the list of audio and transcription logs that have been stored for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
sas_validity_in_seconds = 56 # int | The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip_token = 'skip_token_example' # str | Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)

try:
    # Gets the list of audio and transcription logs that have been stored for a given endpoint.
    api_response = api_instance.endpoints_list_logs(id, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_list_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **sas_validity_in_seconds** | **int**| The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip_token** | **str**| Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list_supported_locales**
> list[str] endpoints_list_supported_locales()

Gets a list of supported locales for endpoint creations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for endpoint creations.
    api_response = api_instance.endpoints_list_supported_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_list_supported_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_update**
> Endpoint endpoints_update(id, endpoint_update)

Updates the metadata of the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
endpoint_update = swagger_client.EndpointUpdate() # EndpointUpdate | The updated values for the endpoint.

try:
    # Updates the metadata of the endpoint identified by the given ID.
    api_response = api_instance.endpoints_update(id, endpoint_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->endpoints_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **endpoint_update** | [**EndpointUpdate**](EndpointUpdate.md)| The updated values for the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

