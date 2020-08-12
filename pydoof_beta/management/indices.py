from pydoof_core import IndicesApi

from pydoof_beta.management.helpers import setup_management_api

__ALL__ = ('Indices')


class Indices():
    @staticmethod
    def list(hashid, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_index(hashid)

    @staticmethod
    def create(hashid, data, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_create(data, hashid).to_dict()

    @staticmethod
    def get(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_show(hashid, name).to_dict()

    @staticmethod
    def update(hashid, name, data, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.index_update(data, hashid, name).to_dict()

    @staticmethod
    def delete(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.index_delete(hashid, name)

    @staticmethod
    def create_temp(hashid, name, **opts):
        query_params = []
        if 'destination_server' in opts:
            query_params += [('destination_server', opts['destination_server'])]

        api_client = setup_management_api(**opts)
        api_client.call_api(
            '/api/v2/search_engines/{hashid}/indices/{name}/temp',
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    def delete_temp(hashid, name, **opts):
        query_params = []
        if 'destination_server' in opts:
            query_params += [('destination_server', opts['destination_server'])]

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
    def reindex_to_temp(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        api_instance.reindex_to_temp(hashid, name)

    @staticmethod
    def reindex_status(hashid, name, **opts):
        api_instance = setup_management_api(IndicesApi, **opts)
        return api_instance.get_reindexing_status(hashid, name)

    @staticmethod
    def replace_by_temp(hashid, name, **opts):
        query_params = []
        if 'destination_server' in opts:
            query_params += [('destination_server', opts['destination_server'])]

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