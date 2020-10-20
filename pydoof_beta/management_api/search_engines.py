from pydoof_beta.management_api.api_client import ManagementApiClient


def _get_searchengines_url():
    return '/api/v2/search_engines'


def _get_searchengine_url(hashid):
    return f'/api/v2/search_engines/{hashid}'


def _get_process_url(hashid):
    return f'/api/v2/search_engines/{hashid}/_process'


def list(**opts):
    api_client = ManagementApiClient(**opts)
    return api_client.get(
        _get_searchengines_url()
    )


def create(data, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.post(
        _get_searchengines_url(),
        data
    )


def get(hashid, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.get(
        _get_searchengine_url(hashid)
    )


def update(hashid, data, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.patch(
        _get_searchengine_url(hashid),
        data
    )


def delete(hashid, **opts):
    api_client = ManagementApiClient(**opts)
    api_client.delete(
        _get_searchengine_url(hashid)
    )


def schedule_process(hashid, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.post(
        _get_process_url(hashid)
    )


def get_process_status(hashid, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.get(
        _get_process_url(hashid)
    )
