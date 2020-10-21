from pydoof_beta.search_api.api_client import SearchAPIClient


def _get_cache_url(hashid):
    return f'/cache/{hashid}'


def cached_config(cls, hashid, **opts):
    api_client = SearchAPIClient(**opts)
    return api_client.get(
        _get_cache_url(hashid) + '/get'
    )


def refresh_config(cls, hashid, **opts):
    api_client = SearchAPIClient(**opts)
    api_client.post(
        _get_cache_url(hashid) + '/refresh'
    )


def delete_config(cls, hashid, **opts):
    api_client = SearchAPIClient(**opts)
    api_client.delete(
        _get_cache_url(hashid) + '/delete'
    )
