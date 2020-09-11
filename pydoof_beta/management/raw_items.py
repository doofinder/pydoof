from pydoof_beta.api_client import ApiClient

__ALL__ = ('RawItems')


class RawItems():
    @staticmethod
    def __class_url(hashid, name):
        return '/api/v2/search_engines/{hashid}/indices/{name}/temp/items',

    @staticmethod
    def __instance_url(hashid, name, item_id):
        return '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/{item_id}',

    def __get_query_params(**opts):
        query_params = {'raw': 1}
        if 'destination_server' in opts:
            query_params['destination_server'] = opts['destination_server']
        return query_params

    @classmethod
    def create(cls, hashid, name, item, **opts):
        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__class_url(hashid, name),
            item,
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def get(cls, hashid, name, item_id, **opts):
        api_client = ApiClient(**opts)
        return api_client.get(
            cls.__instance_url(hashid, name, item_id),
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def update(cls, hashid, name, item_id, item, **opts):
        api_client = ApiClient(**opts)
        return api_client.patch(
            cls.__instance_url(hashid, name, item_id),
            item,
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def delete(cls, hashid, name, item_id, **opts):
        api_client = ApiClient(**opts)
        api_client.delete(
            cls.__instance_url(hashid, name, item_id),
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def mget(cls, hashid, name, items, **opts):
        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__class_url(hashid, name),
            items,
            query_params=cls.__get_query_params(**opts)
        )

    @classmethod
    def bulk_create(cls, hashid, name, items, **opts):
        api_client = ApiClient(**opts)
        return api_client.post(
            cls.__class_url(hashid, name) + '/_bulk',
            items,
            cls.__query_params(**opts)
        )

    @classmethod
    def bulk_delete(cls, hashid, name, items, temp=False, **opts):
        api_client = ApiClient(**opts)
        return api_client.delete(
            cls.__class_url(hashid, name) + '/_bulk',
            items,
            cls.__query_params(**opts)
        )

    @classmethod
    def bulk_update(cls, hashid, name, items, temp=False, **opts):
        api_client = ApiClient(**opts)
        return api_client.patch(
            cls.__class_url(hashid, name) + '/_bulk',
            items,
            cls.__query_params(**opts)
        )
