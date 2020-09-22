from pydoof_beta.api_client import ApiClient

__ALL__ = ('Indices')


class Indices():
    @staticmethod
    def __class_url(hashid):
        return f'/api/v2/search_engines/{hashid}/indices'

    @staticmethod
    def __instance_url(hashid, name):
        return f'/api/v2/search_engines/{hashid}/indices/{name}'

    @classmethod
    def list(cls, hashid, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__class_url(hashid)
        )

    @classmethod
    def create(cls, hashid, data, **opts):
        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__class_url(hashid),
            data
        )

    @classmethod
    def get(cls, hashid, name, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__instance_url(hashid, name)
        )

    @classmethod
    def update(cls, hashid, name, data, **opts):
        api_client = ApiClient(**opts)
        return api_client.patch(
            cls.__instance_url(hashid, name),
            data
        )

    @classmethod
    def delete(cls, hashid, name, **opts):
        api_client = ApiClient(**opts)
        api_client.delete(
            cls.__instance_url(hashid, name)
        )

    @classmethod
    def create_temp(cls, hashid, name, **opts):
        params = {}
        if 'destination_server' in opts:
            params['destination_server'] = opts['destination_server']

        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__instance_url(hashid, name) + '/temp',
            query_params=params
        )

    @classmethod
    def delete_temp(cls, hashid, name, **opts):
        params = {}
        if 'destination_server' in opts:
            params['destination_server'] = opts['destination_server']

        api_client = ApiClient(**opts)
        api_client.delete(
            cls.__instance_url(hashid, name) + '/temp',
            query_params=params
        )

    @classmethod
    def reindex_to_temp(cls, hashid, name, **opts):
        params = {}
        if 'destination_server' in opts:
            params['destination_server'] = opts['destination_server']

        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__instance_url(hashid, name) + '/_reindex_to_temp',
            query_params=params
        )

    @classmethod
    def reindex_status(cls, hashid, name, **opts):
        params = {}
        if 'destination_server' in opts:
            params['destination_server'] = opts['destination_server']

        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__instance_url(hashid, name) + '/_reindex_to_temp',
            query_params=params
        )

    @classmethod
    def replace_by_temp(cls, hashid, name, **opts):
        params = {}
        if 'destination_server' in opts:
            params['destination_server'] = opts['destination_server']

        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__instance_url(hashid, name) + '/_replace_by_temp',
            query_params=params
        )
