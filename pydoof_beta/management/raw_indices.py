from pydoof_beta.api_client import ApiClient

__ALL__ = ('RawIndices')


class RawIndices():
    @staticmethod
    def __class_url(hashid, name):
        return f'/api/v2/search_engines/{hashid}/indices/{name}'

    @staticmethod
    def __get_query_params(**opts):
        query_params = {'raw': 1}
        if 'destination_server' in opts:
            query_params['destination_server'] = opts['destination_server']
        return query_params

    @classmethod
    def create_temp(cls, hashid, name, index_config, **opts):
        api_client = ApiClient(**opts)
        api_client.post(
            cls.__class_url(hashid, name) + '/temp',
            index_config,
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def delete_temp(cls, hashid, name, **opts):
        api_client = ApiClient(**opts)
        api_client.delete(
            cls.__class_url(hashid, name) + '/temp',
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def reindex_to_temp(cls, hashid, name, **opts):
        api_client = ApiClient(**opts)
        api_client.post(
            cls.__class_url(hashid, name) + '/_reindex_to_temp',
            query_params={'raw': 1}
        )

    @classmethod
    def reindex_status(cls, hashid, name, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__class_url(hashid, name) + '/_reindex_to_temp',
            query_params={'raw': 1}
        )

    @classmethod
    def replace_by_temp(cls, hashid, name, **opts):
        api_client = ApiClient(**opts)
        api_client.post(
            cls.__class_url(hashid, name) + '/_replace_by_temp',
            query_params=cls.__get_query_params(**opts)
        )
