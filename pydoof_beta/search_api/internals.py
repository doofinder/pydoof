from pydoof_beta.api_client import SearchApiClient

__ALL__ = ('Internals')


class Internals():
    @staticmethod
    def __cache_url(hashid):
        return f'/cache/{hashid}'

    @classmethod
    def cached_config(cls, hashid, **opts):
        api_client = SearchApiClient(**opts)
        return api_client.get(
            cls.__cache_url(hashid) + '/get'
        )

    @classmethod
    def refresh_config(cls, hashid, **opts):
        api_client = SearchApiClient(**opts)
        api_client.post(
            cls.__cache_url(hashid) + '/refresh'
        )

    @classmethod
    def delete_config(cls, hashid, **opts):
        api_client = SearchApiClient(**opts)
        api_client.delete(
            cls.__cache_url(hashid) + '/delete'
        )
