from pydoof_beta.management.helpers import (handle_api_errors,
                                            setup_management_api)

__ALL__ = ('RawIndices')


class RawIndices():
    @staticmethod
    @handle_api_errors
    def create_temp(hashid, name, index_config, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp',
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            body=index_config,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def delete_temp(hashid, name, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp',
            'DELETE',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def reindex_to_temp(hashid, name, **opts):
        api_client = setup_management_api(**opts)
        api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/_reindex_to_temp',
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=[('raw', 1)],
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def reindex_status(hashid, name, **opts):
        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/_reindex_to_temp',
            'GET',
            path_params={'hashid': hashid, 'name': name},
            query_params=[('raw', 1)],
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def replace_by_temp(hashid, name, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/_replace_by_temp',
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )
