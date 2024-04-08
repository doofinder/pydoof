from pydoof.helpers import parse_query_params
from pydoof.management_api.api_client import ManagementAPIClient


def _get_user_url(user_id):
    return f"/api/v2/internal/users/{user_id}"


def _get_searchengine_url(searchengine_hashid):
    return f"/api/v2/internal/search_engines/{searchengine_hashid}"


def users_refresh(user_id, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    api_client.post(_get_user_url(user_id) + "/refresh")


def searchengine_refresh(searchengine_hashid, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    api_client.post(_get_searchengine_url(searchengine_hashid) + "/refresh")


def set_searchengine_replicas(searchengine_hashid, replicas, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    api_client.post(
        _get_searchengine_url(searchengine_hashid) + "/replicas",
        json={"replicas": replicas},
    )


def delete_stored_specs(searchengine_hashid, stored_spec_key, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.delete(
        _get_searchengine_url(searchengine_hashid) + "/stored_specs",
        query_params=parse_query_params({"stored_spec": stored_spec_key}),
    )


def get_stored_specs(searchengine_hashid, stored_spec_key, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + "/stored_specs",
        query_params=parse_query_params({"stored_spec": stored_spec_key}),
    )


def searchengine_mappings(searchengine_hashid, indices=None, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + "/mappings",
        query_params=parse_query_params({"indices": indices}),
    )


def facets_terms(searchengine_hashid, fields, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(
        _get_searchengine_url(searchengine_hashid) + "/facets_terms",
        query_params=parse_query_params({"fields": fields}),
    )


def searchengine_stats_blocked_ips(searchengine_hashid, client=None, **opts):
    api_client = client or ManagementAPIClient(**opts)
    return api_client.get(_get_searchengine_url(searchengine_hashid) + "/stats_blocked_ips")
