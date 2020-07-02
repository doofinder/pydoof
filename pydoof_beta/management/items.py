from pydoof_core import ItemsApi

from pydoof_beta.management.helpers import setup_management_api

__ALL__ = ('Items', 'Scroll')


class Scroll():

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
            scroll = self.next()

    def new(self):
        api_instance = setup_management_api(ItemsApi, **self.opts)
        scroll_page = api_instance.item_index(
            self.hashid, self.name, rpp=self.rpp
        ).to_dict()
        self.scroll_id = scroll_page['scroll_id']
        return scroll_page

    def next(self):
        api_instance = setup_management_api(ItemsApi, **self.opts)
        return api_instance.item_index(
            self.hashid, self.name, scroll_id=self.scroll_id, rpp=self.rpp
        ).to_dict()


class Items():

    @staticmethod
    def scroll(hashid, name, rpp=None, **opts):
        return Scroll(hashid, name, rpp, **opts)

    @staticmethod
    def create(hashid, name, item, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            return api_instance.item_temp_create(item, hashid, name)
        return api_instance.item_create(item, hashid, name)

    @staticmethod
    def get(hashid, name, item_id, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            return api_instance.item_temp_show(hashid, name, item_id)
        return api_instance.item_show(hashid, name, item_id)

    @staticmethod
    def mget(hashid, name, items, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            return api_instance.items_temp_mget(items, hashid, name)
        return api_instance.items_mget(items, hashid, name)

    @staticmethod
    def update(hashid, name, item_id, item, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            return api_instance.item_temp_update(item, hashid, name, item_id)
        return api_instance.item_update(item, hashid, name, item_id)

    @staticmethod
    def delete(hashid, name, item_id, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            api_instance.item_temp_delete(hashid, name, item_id)
        api_instance.item_delete(hashid, name, item_id)

    @staticmethod
    def bulk_create(hashid, name, items, temp=False, **opts):
        query_params = []
        if 'destination_server' in opts:
            query_params += [('destination_server', opts['destination_server'])]

        url = '/api/v2/search_engines/{hashid}/indices/{name}/items/_bulk'
        if temp:
            url = '/api/v2/search_engines/{hashid}/indices/{name}/temp/items/_bulk'

        api_client = setup_management_api(**opts)
        api_client.call_api(
            url,
            'POST',
            path_params={'hashid': hashid, 'name': name},
            query_params=query_params,
            body=items,
            auth_settings=['api_token'],
            response_type='object',
            _return_http_data_only=True
        )

    @staticmethod
    def bulk_delete(hashid, name, items, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            return api_instance.items_temp_bulk_delete(items, hashid, name)
        return api_instance.items_bulk_delete(items, hashid, name)

    @staticmethod
    def bulk_update(hashid, name, items, temp=False, **opts):
        api_instance = setup_management_api(ItemsApi, **opts)
        if temp:
            return api_instance.items_temp_bulk_update(items, hashid, name)
        return api_instance.items_bulk_update(items, hashid, name)
