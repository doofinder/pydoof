from pydoof_beta.management.helpers import (bulk_request,
                                            handle_api_errors,
                                            setup_management_api)

__ALL__ = ('RawItems')


class RawItems():
    @staticmethod
    @handle_api_errors
    def create(hashid, name, item, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp/items',
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            body=item,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def get(hashid, name, item_id, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/{item_id}',
            'GET',
            path_params={'hashid': hashid, 'name': name, 'item_id': item_id},
            query_params=query_params,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def update(hashid, name, item_id, item, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/{item_id}',
            'PATCH',
            path_params={'hashid': hashid, 'name': name, 'item_id': item_id},
            query_params=query_params,
            body=item,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def delete(hashid, name, item_id, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/{item_id}',
            'DELETE',
            path_params={'hashid': hashid, 'name': name, 'item_id': item_id},
            query_params=query_params,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def mget(hashid, name, items, **opts):
        query_params = [('raw', 1)]
        if 'destination_server' in opts:
            query_params += [
                ('destination_server', opts['destination_server'])
            ]

        api_client = setup_management_api(**opts)
        return api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/_mget',
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            body=items,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    @handle_api_errors
    def bulk_create(hashid, name, items, temp=False, **opts):
        return bulk_request(hashid, name, items, temp, 'POST', raw=True,
                            **opts)

    @staticmethod
    @handle_api_errors
    def bulk_delete(hashid, name, items, temp=False, **opts):
        return bulk_request(hashid, name, items, temp, 'DELETE', raw=True,
                            **opts)

    @staticmethod
    @handle_api_errors
    def bulk_update(hashid, name, items, temp=False, **opts):
        return bulk_request(hashid, name, items, temp, 'PATCH', raw=True,
                            **opts)
