from pydoof.management_api.api_client import ManagementAPIClient


def _get_index_url(hashid, name):
    return f'/api/v2/search_engines/{hashid}/indices/{name}'


def _get_query_params(**opts):
    query_params = {'raw': None}
    if 'destination_server' in opts:
        query_params['destination_server'] = opts['destination_server']
    return query_params


def create_temp(hashid, name, index_config, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.post(
        _get_index_url(hashid, name) + '/temp',
        index_config,
        query_params=_get_query_params(**opts)
    )


def delete_temp(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.delete(
        _get_index_url(hashid, name) + '/temp',
        query_params=_get_query_params(**opts)
    )


def reindex_to_temp(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.post(
        _get_index_url(hashid, name) + '/_reindex_to_temp',
        query_params={'raw': 1}
    )


def get_reindex_status(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_index_url(hashid, name) + '/_reindex_to_temp',
        query_params={'raw': 1}
    )


def replace_by_temp(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.post(
        _get_index_url(hashid, name) + '/_replace_by_temp',
        query_params=_get_query_params(**opts)
    )
