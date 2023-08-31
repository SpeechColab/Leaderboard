# swagger_client.CustomSpeechWebHooksApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**web_hooks_create**](CustomSpeechWebHooksApi.md#web_hooks_create) | **POST** /webhooks | Creates a new web hook.
[**web_hooks_delete**](CustomSpeechWebHooksApi.md#web_hooks_delete) | **DELETE** /webhooks/{id} | Deletes the web hook identified by the given ID.
[**web_hooks_get**](CustomSpeechWebHooksApi.md#web_hooks_get) | **GET** /webhooks/{id} | Gets the web hook identified by the given ID.
[**web_hooks_list**](CustomSpeechWebHooksApi.md#web_hooks_list) | **GET** /webhooks | Gets the list of web hooks for the authenticated subscription.
[**web_hooks_ping**](CustomSpeechWebHooksApi.md#web_hooks_ping) | **POST** /webhooks/{id}:ping | Sends a ping event to the registered URL.
[**web_hooks_test**](CustomSpeechWebHooksApi.md#web_hooks_test) | **POST** /webhooks/{id}:test | Sends a request for each registered event type to the registered URL.
[**web_hooks_update**](CustomSpeechWebHooksApi.md#web_hooks_update) | **PATCH** /webhooks/{id} | Updates the web hook identified by the given ID.


# **web_hooks_create**
> WebHook web_hooks_create(web_hook)

Creates a new web hook.

If the property secret in the configuration is present and contains a non-empty string, it will be used to create a SHA256 hash of the payload with  the secret as HMAC key. This hash will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.                When calling back into the registered URL, the request will contain a X-MicrosoftSpeechServices-Event header containing one of the registered event  types. There will be one request per registered event type.                After successfully registering the web hook, it will not be usable until a challenge/response is completed. To do this, a request with the event type  challenge will be made with a query parameter called validationToken. Respond to the challenge with a 200 OK containing the value of the validationToken  query parameter as the response body. When the challenge/response is successfully completed, the web hook will begin receiving events.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
web_hook = swagger_client.WebHook() # WebHook | The details of the new web hook.

try:
    # Creates a new web hook.
    api_response = api_instance.web_hooks_create(web_hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook** | [**WebHook**](WebHook.md)| The details of the new web hook. | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_delete**
> web_hooks_delete(id)

Deletes the web hook identified by the given ID.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the web hook.

try:
    # Deletes the web hook identified by the given ID.
    api_instance.web_hooks_delete(id)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the web hook. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_get**
> WebHook web_hooks_get(id)

Gets the web hook identified by the given ID.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the web hook.

try:
    # Gets the web hook identified by the given ID.
    api_response = api_instance.web_hooks_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the web hook. | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_list**
> PaginatedWebHooks web_hooks_list(skip=skip, top=top, filter=filter)

Gets the list of web hooks for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)
filter = 'filter_example' # str | A filtering expression for selecting a subset of the available hooks.              Supported properties: displayName, description, createdDateTime, lastActionDateTime, status and webUrl.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=displayName eq 'test' (optional)

try:
    # Gets the list of web hooks for the authenticated subscription.
    api_response = api_instance.web_hooks_list(skip=skip, top=top, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 
 **filter** | **str**| A filtering expression for selecting a subset of the available hooks.              Supported properties: displayName, description, createdDateTime, lastActionDateTime, status and webUrl.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter&#x3D;displayName eq &#39;test&#39; | [optional] 

### Return type

[**PaginatedWebHooks**](PaginatedWebHooks.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_ping**
> web_hooks_ping(id)

Sends a ping event to the registered URL.

The request body of the POST request sent to the registered web hook URL is of the same shape as in the GET request for a specific hook.  The Swagger Schema ID of the model is WebHookV3.                The request will contain a X-MicrosoftSpeechServices-Event header with the value ping. If the web hook was registered with  a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with  the secret as HMAC key. The hash is base64 encoded.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the web hook to ping.

try:
    # Sends a ping event to the registered URL.
    api_instance.web_hooks_ping(id)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the web hook to ping. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_test**
> web_hooks_test(id)

Sends a request for each registered event type to the registered URL.

The payload will be generated from the last entity that would have invoked the web hook. If no entity is present for none of the registered event types,  the POST will respond with 204. If a test request can be made, it will respond with 200.  The request will contain a X-MicrosoftSpeechServices-Event header with the respective registered event type.  If the web hook was registered with a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with  the secret as HMAC key. The hash is base64 encoded.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the web hook to ping.

try:
    # Sends a request for each registered event type to the registered URL.
    api_instance.web_hooks_test(id)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the web hook to ping. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_update**
> WebHook web_hooks_update(id, web_hook_update)

Updates the web hook identified by the given ID.

If the property secret in the configuration is omitted or contains an empty string, future callbacks won't contain X-MicrosoftSpeechServices-Signature  headers. If the property contains a non-empty string, it will be used to create a SHA256 hash of the payload with the secret as HMAC key. This hash  will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.                If the URL changes,  the web hook will stop receiving events until a  challenge/response is completed. To do this, a request with the event type challenge will be made with a query parameter called validationToken.  Respond to the challenge with a 200 OK containing the value of the validationToken query parameter as the response body. When the challenge/response  is successfully completed, the web hook will begin receiving events.

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
api_instance = swagger_client.CustomSpeechWebHooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the web hook.
web_hook_update = swagger_client.WebHookUpdate() # WebHookUpdate | The updated values for the web hook.

try:
    # Updates the web hook identified by the given ID.
    api_response = api_instance.web_hooks_update(id, web_hook_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechWebHooksApi->web_hooks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the web hook. | 
 **web_hook_update** | [**WebHookUpdate**](WebHookUpdate.md)| The updated values for the web hook. | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

