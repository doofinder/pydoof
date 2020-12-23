from unittest import mock
import unittest

from pydoof.search_api import stats


class TestStats(unittest.TestCase):

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_add_to_cart(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        session_id = '4affa6'
        amount = 2
        item_id = 1235
        title = 'Product'
        price = 12.99

        stats.add_to_cart(
            hashid, index_name, session_id, item_id, amount, title, price
        )

        APIClientMock.return_value.get.assert_called_once_with(
            '/5/stats/add-to-cart',
            {'hashid': hashid, 'datatype': index_name,
             'session_id': session_id, 'item_id': item_id, 'amount': amount,
             'title': title, 'price': price}
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_remove_from_cart(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        session_id = '4affa6'
        amount = 2
        item_id = 1235

        stats.remove_from_cart(
            hashid, index_name, session_id, item_id, amount
        )

        APIClientMock.return_value.get.assert_called_once_with(
            '/5/stats/remove-from-cart',
            {'hashid': hashid, 'datatype': index_name,
             'session_id': session_id, 'item_id': item_id, 'amount': amount}
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_clear_cart(self, APIClientMock):
        hashid = 'aab32d8'
        session_id = '4affa6'

        stats.clear_cart(hashid, session_id)

        APIClientMock.return_value.get.assert_called_once_with(
            '/5/stats/clear-cart',
            {'hashid': hashid, 'session_id': session_id}
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_checkout(self, APIClientMock):
        hashid = 'aab32d8'
        session_id = '4affa6'

        stats.checkout(hashid, session_id)

        APIClientMock.return_value.get.assert_called_once_with(
            '/5/stats/checkout',
            {'hashid': hashid, 'session_id': session_id}
        )
