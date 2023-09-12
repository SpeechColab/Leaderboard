# coding: utf-8

"""
    Speech Services API v3.1
"""


from __future__ import absolute_import

# python 2 and python 3 compatibility library
import six

from batch_client.api_client import ApiClient


class CustomSpeechTranscriptionsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transcriptions_create(self, transcription, **kwargs):
        """Creates a new transcription.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_create(transcription, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Transcription transcription: The details of the new transcription. (required)
        :return: Transcription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_create_with_http_info(transcription, **kwargs)
        else:
            (data) = self.transcriptions_create_with_http_info(transcription, **kwargs)
            return data

    def transcriptions_create_with_http_info(self, transcription, **kwargs):
        """Creates a new transcription.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_create_with_http_info(transcription, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Transcription transcription: The details of the new transcription. (required)
        :return: Transcription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transcription']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transcription' is set
        if self.api_client.client_side_validation and ('transcription' not in params or
                                                       params['transcription'] is None):
            raise ValueError("Missing the required parameter `transcription` when calling `transcriptions_create`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transcription' in params:
            body_params = params['transcription']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transcription',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_delete(self, id, **kwargs):
        """Deletes the specified transcription task.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.transcriptions_delete_with_http_info(id, **kwargs)
            return data

    def transcriptions_delete_with_http_info(self, id, **kwargs):
        """Deletes the specified transcription task.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transcriptions_delete`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_get(self, id, **kwargs):
        """Gets the transcription identified by the given ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :return: Transcription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_get_with_http_info(id, **kwargs)
        else:
            (data) = self.transcriptions_get_with_http_info(id, **kwargs)
            return data

    def transcriptions_get_with_http_info(self, id, **kwargs):
        """Gets the transcription identified by the given ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :return: Transcription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transcriptions_get`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transcription',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_get_file(self, id, file_id, **kwargs):
        """Gets one specific file (identified with fileId) from a transcription (identified with id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_get_file(id, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :param str file_id: The identifier of the file. (required)
        :param int sas_validity_in_seconds: The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated.
        :return: File
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_get_file_with_http_info(id, file_id, **kwargs)
        else:
            (data) = self.transcriptions_get_file_with_http_info(id, file_id, **kwargs)
            return data

    def transcriptions_get_file_with_http_info(self, id, file_id, **kwargs):
        """Gets one specific file (identified with fileId) from a transcription (identified with id).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_get_file_with_http_info(id, file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :param str file_id: The identifier of the file. (required)
        :param int sas_validity_in_seconds: The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated.
        :return: File
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'file_id', 'sas_validity_in_seconds']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_get_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transcriptions_get_file`")
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in params or
                                                       params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `transcriptions_get_file`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']

        query_params = []
        if 'sas_validity_in_seconds' in params:
            query_params.append(('sasValidityInSeconds', params['sas_validity_in_seconds']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions/{id}/files/{fileId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='File',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_list(self, **kwargs):
        """Gets a list of transcriptions for the authenticated subscription.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: Number of datasets that will be skipped.
        :param int top: Number of datasets that will be included after skipping.
        :param str filter: A filtering expression for selecting a subset of the available transcriptions.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=createdDateTime gt 2022-02-01T11:00:00Z
        :return: PaginatedTranscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_list_with_http_info(**kwargs)
        else:
            (data) = self.transcriptions_list_with_http_info(**kwargs)
            return data

    def transcriptions_list_with_http_info(self, **kwargs):
        """Gets a list of transcriptions for the authenticated subscription.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: Number of datasets that will be skipped.
        :param int top: Number of datasets that will be included after skipping.
        :param str filter: A filtering expression for selecting a subset of the available transcriptions.              - Supported properties: displayName, description, createdDateTime, lastActionDateTime, status, locale.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime and lastActionDateTime.                - and, or, not are supported.              - Example:                filter=createdDateTime gt 2022-02-01T11:00:00Z
        :return: PaginatedTranscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'top', 'filter']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))
        if 'top' in params:
            query_params.append(('top', params['top']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedTranscriptions',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_list_files(self, id, **kwargs):
        """Gets the files of the transcription identified by the given ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_list_files(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :param int sas_validity_in_seconds: The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated.
        :param int skip: Number of datasets that will be skipped.
        :param int top: Number of datasets that will be included after skipping.
        :param str filter: A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter=name eq 'myaudio.wav.json' and kind eq 'Transcription'
        :return: PaginatedFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_list_files_with_http_info(id, **kwargs)
        else:
            (data) = self.transcriptions_list_files_with_http_info(id, **kwargs)
            return data

    def transcriptions_list_files_with_http_info(self, id, **kwargs):
        """Gets the files of the transcription identified by the given ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_list_files_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :param int sas_validity_in_seconds: The duration in seconds that an SAS url should be valid. The default duration is 12 hours. When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated.
        :param int skip: Number of datasets that will be skipped.
        :param int top: Number of datasets that will be included after skipping.
        :param str filter: A filtering expression for selecting a subset of the available files.              - Supported properties: name, createdDateTime, kind.              - Operators:                - eq, ne are supported for all properties.                - gt, ge, lt, le are supported for createdDateTime.                - and, or, not are supported.              - Example:                filter=name eq 'myaudio.wav.json' and kind eq 'Transcription'
        :return: PaginatedFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'sas_validity_in_seconds', 'skip', 'top', 'filter']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_list_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transcriptions_list_files`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'sas_validity_in_seconds' in params:
            query_params.append(('sasValidityInSeconds', params['sas_validity_in_seconds']))
        if 'skip' in params:
            query_params.append(('skip', params['skip']))
        if 'top' in params:
            query_params.append(('top', params['top']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions/{id}/files', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedFiles',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_list_supported_locales(self, **kwargs):
        """Gets a list of supported locales for offline transcriptions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_list_supported_locales(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_list_supported_locales_with_http_info(**kwargs)
        else:
            (data) = self.transcriptions_list_supported_locales_with_http_info(**kwargs)
            return data

    def transcriptions_list_supported_locales_with_http_info(self, **kwargs):
        """Gets a list of supported locales for offline transcriptions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_list_supported_locales_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_list_supported_locales" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions/locales', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transcriptions_update(self, id, transcription_update, **kwargs):
        """Updates the mutable details of the transcription identified by its ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_update(id, transcription_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :param TranscriptionUpdate transcription_update: The updated values for the transcription. (required)
        :return: Transcription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transcriptions_update_with_http_info(id, transcription_update, **kwargs)
        else:
            (data) = self.transcriptions_update_with_http_info(id, transcription_update, **kwargs)
            return data

    def transcriptions_update_with_http_info(self, id, transcription_update, **kwargs):
        """Updates the mutable details of the transcription identified by its ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transcriptions_update_with_http_info(id, transcription_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The identifier of the transcription. (required)
        :param TranscriptionUpdate transcription_update: The updated values for the transcription. (required)
        :return: Transcription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'transcription_update']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transcriptions_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `transcriptions_update`")
        # verify the required parameter 'transcription_update' is set
        if self.api_client.client_side_validation and ('transcription_update' not in params or
                                                       params['transcription_update'] is None):
            raise ValueError("Missing the required parameter `transcription_update` when calling `transcriptions_update`")

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transcription_update' in params:
            body_params = params['transcription_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json', 'application/merge-patch+json'])

        # Authentication setting
        auth_settings = ['api_key', 'token']

        return self.api_client.call_api(
            '/transcriptions/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transcription',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
