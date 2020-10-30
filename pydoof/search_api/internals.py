from pydoof.search_api.api_client import SearchAPIClient


def refresh_config(cls, hashid, **opts):
    api_client = SearchAPIClient(**opts)
    api_client.post(
        f'/cache/{hashid}/refresh'
    )
