from unittest import mock
import unittest

from pydoof.management_api import items
from pydoof.management_api.exceptions import TooManyRequestsError


class TestScroll(unittest.TestCase):

    @mock.patch('pydoof.management_api.items.sleep')
    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_scroll_iteration(self, APIClientMock, _sleep_mock):
        scroll_id = 'c4011d'
        hashid = 'aab32d8'
        index_name = 'product'
        rpp = 5
        APIClientMock.return_value.get.side_effect = [
            {'scroll_id': scroll_id, 'items': [0, 1, 2, 3, 4]},
            TooManyRequestsError(),
            TooManyRequestsError(),
            {'scroll_id': scroll_id, 'items': [5, 6, 7, 8, 9]},
            {'scroll_id': scroll_id, 'items': []}
        ]

        scroll = items.Scroll(hashid, index_name, rpp)

        self.assertEqual(list(item for item in scroll), list(range(10)))

        url = '/api/v2/search_engines/aab32d8/indices/product/items/'
        first_call = mock.call(url, {'rpp': 5})
        next_call = mock.call(url, {'scroll_id': scroll_id, 'rpp': 5})

        APIClientMock.return_value.get.assert_has_calls([
            first_call, next_call, next_call, next_call, next_call
        ])

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_scroll_pages(self, APIClientMock):
        scroll_id = 'c4011d'
        hashid = 'aab32d8'
        index_name = 'product'
        rpp = 5
        first_page = {'scroll_id': scroll_id, 'items': [0, 1, 2, 3, 4]}
        second_page = {'scroll_id': scroll_id, 'items': [5, 6, 7, 8, 9]}
        last_page = {'scroll_id': scroll_id, 'items': []}
        APIClientMock.return_value.get.side_effect = [
            first_page, second_page, last_page
        ]

        scroll = items.Scroll(hashid, index_name, rpp)

        self.assertEqual(scroll.new(), first_page)
        self.assertEqual(scroll.next(), second_page)
        self.assertEqual(scroll.next(), last_page)

        url = '/api/v2/search_engines/aab32d8/indices/product/items/'
        first_call = mock.call(url, {'rpp': 5})
        next_call = mock.call(url, {'scroll_id': scroll_id, 'rpp': 5})

        APIClientMock.return_value.get.assert_has_calls([
            first_call, next_call, next_call
        ])


class TestItems(unittest.TestCase):
    @mock.patch('pydoof.management_api.items.Scroll')
    def test_scroll(self, ScrollMock):
        hashid = 'aab32d8'
        index_name = 'product'
        rpp = 5

        items.scroll(hashid, index_name, rpp=rpp)
        ScrollMock.assert_called_once_with(
            hashid, index_name, rpp
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_create(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item = {'item': 'ITEM'}

        items.create(hashid, index_name, item)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/items',
            item
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_create_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item = {'item': 'ITEM'}

        items.create(hashid, index_name, item, temp=True)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp/items',
            item
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_get(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item_id = '1235'

        items.get(hashid, index_name, item_id)

        APIClientMock.return_value.get.assert_called_with(
            f'/api/v2/search_engines/aab32d8/indices/product/items/{item_id}',
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_get_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item_id = '1235'

        items.get(hashid, index_name, item_id, temp=True)

        APIClientMock.return_value.get.assert_called_with(
            f'/api/v2/search_engines/aab32d8/indices/product/temp/items/{item_id}'
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_update(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item_id = '1235'
        item = {'item': 'ITEM'}

        items.update(hashid, index_name, item_id, item)

        APIClientMock.return_value.patch.assert_called_with(
            f'/api/v2/search_engines/aab32d8/indices/product/items/{item_id}',
            item
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_update_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item_id = '1235'
        item = {'item': 'ITEM'}

        items.update(hashid, index_name, item_id, item, temp=True)

        APIClientMock.return_value.patch.assert_called_with(
            f'/api/v2/search_engines/aab32d8/indices/product/temp/items/{item_id}',
            item
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_delete(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item_id = '1235'

        items.delete(hashid, index_name, item_id)

        APIClientMock.return_value.delete.assert_called_with(
            f'/api/v2/search_engines/aab32d8/indices/product/items/{item_id}'
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_delete_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        item_id = '1235'

        items.delete(hashid, index_name, item_id, temp=True)

        APIClientMock.return_value.delete.assert_called_with(
            f'/api/v2/search_engines/aab32d8/indices/product/temp/items/{item_id}'
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_find(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_ids = {'id': '1235'}

        items.find(hashid, index_name, items_ids)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/items/_mget',
            items_ids
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_find_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_ids = ['item_id']

        items.find(hashid, index_name, items_ids, temp=True)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp/items/_mget',
            items_ids
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_bulk_create(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_data = ['item']

        items.bulk_create(hashid, index_name, items_data)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/items/_bulk',
            items_data
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_bulk_create_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_data = ['item']

        items.bulk_create(hashid, index_name, items_data, temp=True)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp/items/_bulk',
            items_data
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_bulk_update(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_data = ['item']

        items.bulk_update(hashid, index_name, items_data)

        APIClientMock.return_value.patch.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/items/_bulk',
            items_data
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_bulk_update_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_data = ['item']

        items.bulk_update(hashid, index_name, items_data, temp=True)

        APIClientMock.return_value.patch.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp/items/_bulk',
            items_data
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_bulk_delete(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_data = ['item']

        items.bulk_delete(hashid, index_name, items_data)

        APIClientMock.return_value.delete.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/items/_bulk',
            items_data
        )

    @mock.patch('pydoof.management_api.items.ManagementAPIClient')
    def test_bulk_delete_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        items_data = ['item']

        items.bulk_delete(hashid, index_name, items_data, temp=True)

        APIClientMock.return_value.delete.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp/items/_bulk',
            items_data
        )
