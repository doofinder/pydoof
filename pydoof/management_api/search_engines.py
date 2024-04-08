from pydoof.management_api.api_client import ManagementAPIClient


def _get_searchengines_url():
    return "/api/v2/search_engines"


def _get_searchengine_url(hashid):
    return f"/api/v2/search_engines/{hashid}"


def _get_process_url(hashid):
    return f"/api/v2/search_engines/{hashid}/_process"


def list(client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(_get_searchengines_url())


def create(search_engine, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.post(_get_searchengines_url(), search_engine)


def get(hashid, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(_get_searchengine_url(hashid))


def update(hashid, search_engine, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.patch(_get_searchengine_url(hashid), search_engine)


def delete(hashid, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    api_client.delete(_get_searchengine_url(hashid))


def schedule_process(hashid, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.post(_get_process_url(hashid))


def get_process_status(hashid, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(_get_process_url(hashid))
