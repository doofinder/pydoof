from pydoof.management_api.api_client import ManagementAPIClient
from pydoof.management_api.exceptions import TooManyRequestsError
from time import sleep


class Scroll():
    @staticmethod
    def __get_url(hashid, name):
        return f'/api/v2/search_engines/{hashid}/indices/{name}/items/'

    def __init__(self, hashid, name, rpp=None, **opts):
        super(Scroll, self).__init__()

        self.scroll_id = None
        self.rpp = rpp

        self.hashid = hashid
        self.name = name

        self.api_client = ManagementAPIClient(**opts)

    def __iter__(self):
        scroll_page = self.new()
        while scroll_page['items']:
            for item in scroll_page['items']:
                yield item
            scroll_page = self.__next_with_retry()

    def __next_with_retry(self):
        tries = 0
        while True:
            try:
                return self.next()
            except TooManyRequestsError:
                if tries < 3:
                    tries += 1
                    sleep(1)
                else:
                    raise

    @property
    def _query_params(self):
        params = {}
        if self.scroll_id:
            params['scroll_id'] = self.scroll_id
        if self.rpp:
            params['rpp'] = self.rpp
        return params

    def new(self):
        scroll_page = self.api_client.get(
            self.__get_url(self.hashid, self.name),
            self._query_params
        )
        self.scroll_id = scroll_page['scroll_id']
        return scroll_page

    def next(self):
        return self.api_client.get(
            self.__get_url(self.hashid, self.name),
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


def scroll(hashid, name, rpp=None, **opts):
    return Scroll(hashid, name, rpp, **opts)


def create(hashid, name, item, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name, temp),
        item
    )


def get(hashid, name, item_id, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.get(
        _get_item_url(hashid, name, item_id, temp)
    )


def update(hashid, name, item_id, item, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.patch(
        _get_item_url(hashid, name, item_id, temp),
        item
    )


def delete(hashid, name, item_id, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    api_client.delete(
        _get_item_url(hashid, name, item_id, temp)
    )


def find(hashid, name, items_ids, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_items_url(hashid, name, temp) + '/_mget',
        items_ids
    )


def bulk_create(hashid, name, items, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.post(
        _get_bulk_url(hashid, name, temp),
        items
    )


def bulk_update(hashid, name, items, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.patch(
        _get_bulk_url(hashid, name, temp),
        items
    )


def bulk_delete(hashid, name, items, temp=False, **opts):
    api_client = ManagementAPIClient(**opts)
    return api_client.delete(
        _get_bulk_url(hashid, name, temp),
        items
    )
