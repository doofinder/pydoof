from pydoof_beta.api_client import ManagementApiClient
from pydoof_beta.helpers import build_query_params


def _get_user_url(user_id):
    return f'/api/v2/internal/users/{user_id}'


def _get_searchengine_url(searchengine_hashid):
    return f'/api/v2/internal/search_engines/{searchengine_hashid}'


def users_refresh(user_id, **opts):
    api_client = ManagementApiClient(**opts)
    api_client.post(
        _get_user_url(user_id) + '/refresh'
    )


def searchengine_refresh(searchengine_hashid, **opts):
    api_client = ManagementApiClient(**opts)
    api_client.post(
        _get_searchengine_url(searchengine_hashid) + '/refresh'
    )


def searchengine_mappings(searchengine_hashid, indices=None, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + '/mappings',
        query_params=build_query_params({'indices': indices})
    )


def searchengine_stats_blocked_ips(searchengine_hashid, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + '/stats_blocked_ips',
    )
