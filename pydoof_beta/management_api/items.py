from pydoof_beta.management_api.api_client import ManagementApiClient
from pydoof_beta.management_api.exceptions import TooManyRequestsError
from time import sleep


class Scroll():
    @staticmethod
    def __url(hashid, name):
        return f'/api/v2/search_engines/{hashid}/indices/{name}/items/'

    def __init__(self, hashid, name, rpp=None, **opts):
        super(Scroll, self).__init__()

        self.scroll_id = None
        self.rpp = rpp

        self.hashid = hashid
        self.name = name

        self.opts = opts

    def __iter__(self):
        scroll = self.new()
        while scroll['items']:
            for item in scroll['items']:
                yield item
            try:
                scroll = self.next()
            except TooManyRequestsError:
                sleep(1000)
                scroll = self.next()

    @property
    def _query_params(self):
        params = {}
        if self.scroll_id:
            params['scroll_id'] = self.scroll_id
        if self.rpp:
            params['rpp'] = self.rpp
        return params

    def new(self):
        api_client = ManagementApiClient(**self.opts)
        scroll_page = api_client.get(
            self.__url(self.hashid, self.name),
            self._query_params
        )
        self.scroll_id = scroll_page['scroll_id']
        return scroll_page

    def next(self):
        api_client = ManagementApiClient(**self.opts)
        return api_client.get(
            self.__url(self.hashid, self.name),
            self._query_params
        )


def _get_items_url(hashid, name, temp=False):
    url = f'/api/v2/search_engines/{hashid}/indices/{name}'
    if temp:
        url += '/temp'
    return url + '/items'


def _get_item_url(hashid, name, item_id, temp=False):
    url = f'/api/v2/search_engines/{hashid}/indices/{name}'
    if temp:
        url += '/temp'
    return url + f'/items/{item_id}'


def _get_bulk_url(hashid, name, temp=False):
    url = f'/api/v2/search_engines/{hashid}/indices/{name}'
    if temp:
        url += '/temp'
    return url + '/items/_bulk'


def _get_query_params(**opts):
    params = {}
    if 'destination_server' in opts:
        params['destination_server'] = opts['destination_server']
    return params


def scroll(hashid, name, rpp=None, **opts):
    return Scroll(hashid, name, rpp, **opts)


def create(hashid, name, item, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name, temp),
        item,
        _get_query_params(**opts)
    )


def get(hashid, name, item_id, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.get(
        _get_item_url(hashid, name, item_id, temp),
        _get_query_params(**opts)
    )


def update(hashid, name, item_id, item, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.patch(
        _get_item_url(hashid, name, item_id, temp),
        item,
        _get_query_params(**opts)
    )


def delete(hashid, name, item_id, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    api_client.delete(
        _get_item_url(hashid, name, item_id, temp),
        _get_query_params(**opts)
    )


def find(hashid, name, items_ids, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name, temp) + '/_mget',
        items_ids,
        _get_query_params(**opts)
    )


def bulk_create(hashid, name, items, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.post(
        _get_bulk_url(hashid, name, temp),
        items,
        _get_query_params(**opts)
    )


def bulk_update(hashid, name, items, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.patch(
        _get_bulk_url(hashid, name, temp),
        items,
        _get_query_params(**opts)
    )


def bulk_delete(hashid, name, items, temp=False, **opts):
    api_client = ManagementApiClient(**opts)
    return api_client.delete(
        _get_bulk_url(hashid, name, temp),
        items,
        _get_query_params(**opts)
    )
