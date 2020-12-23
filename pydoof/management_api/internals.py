from pydoof.management_api.api_client import ManagementAPIClient
from pydoof.helpers import parse_query_params


def _get_user_url(user_id):
    return f'/api/v2/internal/users/{user_id}'


def _get_searchengine_url(searchengine_hashid):
    return f'/api/v2/internal/search_engines/{searchengine_hashid}'


def users_refresh(user_id, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.post(
        _get_user_url(user_id) + '/refresh'
    )


def searchengine_refresh(searchengine_hashid, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.post(
        _get_searchengine_url(searchengine_hashid) + '/refresh'
    )


def set_searchengine_replicas(searchengine_hashid, replicas, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.post(
        _get_searchengine_url(searchengine_hashid) + '/replicas',
        json={'replicas': replicas}
    )


def searchengine_mappings(searchengine_hashid, indices=None, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + '/mappings',
        query_params=parse_query_params({'indices': indices})
    )


def facets_terms(searchengine_hashid, fields, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + '/facets_terms',
        query_params=parse_query_params({'fields': fields})
    )


def searchengine_stats_blocked_ips(searchengine_hashid, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + '/stats_blocked_ips'
    )
