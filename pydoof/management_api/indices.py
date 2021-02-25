from pydoof.management_api.api_client import ManagementAPIClient


def _get_indices_url(hashid):
    return f'/api/v2/search_engines/{hashid}/indices'


def _get_index_url(hashid, name):
    return f'/api/v2/search_engines/{hashid}/indices/{name}'


def list(hashid, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_indices_url(hashid)
    )


def create(hashid, index, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_indices_url(hashid),
        index
    )


def get(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_index_url(hashid, name)
    )


def update(hashid, name, index, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.patch(
        _get_index_url(hashid, name),
        index
    )


def delete(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.delete(
        _get_index_url(hashid, name)
    )


def create_temp(hashid, name, **opts):
    params = {}
    if 'destination_server' in opts:
        params['destination_server'] = opts['destination_server']

    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_index_url(hashid, name) + '/temp',
        query_params=params
    )


def delete_temp(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.delete(
        _get_index_url(hashid, name) + '/temp'
    )


def reindex_to_temp(hashid, name, **opts):
    params = {}
    if 'reset' in opts:
        params['reset'] = opts['reset']

    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_index_url(hashid, name) + '/_reindex_to_temp',
        query_params=params
    )


def get_reindex_status(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_index_url(hashid, name) + '/_reindex_to_temp'
    )


def replace_by_temp(hashid, name, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_index_url(hashid, name) + '/_replace_by_temp'
    )
