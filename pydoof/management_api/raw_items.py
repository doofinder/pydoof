from pydoof.management_api.api_client import ManagementAPIClient


def _get_items_url(hashid, name):
    return f'/api/v2/search_engines/{hashid}/indices/{name}/temp/items'


def _get_item_url(hashid, name, item_id):
    return f'/api/v2/search_engines/{hashid}/indices/{name}/temp/items/{item_id}'


def _get_query_params(**opts):
    query_params = {'raw': 1}
    if 'destination_server' in opts:
        query_params['destination_server'] = opts['destination_server']
    return query_params


def create(hashid, name, item, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name),
        item,
        query_params=_get_query_params(**opts)
    )


def get(hashid, name, item_id, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_item_url(hashid, name, item_id),
        query_params=_get_query_params(**opts)
    )


def update(hashid, name, item_id, item, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.patch(
        _get_item_url(hashid, name, item_id),
        item,
        query_params=_get_query_params(**opts)
    )


def delete(hashid, name, item_id, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.delete(
        _get_item_url(hashid, name, item_id),
        query_params=_get_query_params(**opts)
    )


def find(hashid, name, items, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name),
        items,
        query_params=_get_query_params(**opts)
    )


def bulk_create(hashid, name, items, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name) + '/_bulk',
        items,
        _get_query_params(**opts)
    )


def bulk_delete(hashid, name, items, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.delete(
        _get_items_url(hashid, name) + '/_bulk',
        items,
        _get_query_params(**opts)
    )


def bulk_update(hashid, name, items, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.patch(
        _get_items_url(hashid, name) + '/_bulk',
        items,
        _get_query_params(**opts)
    )
