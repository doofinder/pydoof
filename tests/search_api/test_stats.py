import unittest
from unittest import mock

from pydoof.search_api import stats


class TestStats(unittest.TestCase):

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_init_session(self, APIClientMock):
        hashid = 'aab32d8'
        session_id = 'SESSION_ID'

        stats.init_session(hashid, session_id)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/init',
            query_params={'session_id': session_id}
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_log_checkout(self, APIClientMock):
        hashid = 'aab32d8'
        session_id = 'SESSION_ID'

        stats.log_checkout(hashid, session_id)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/checkout',
            query_params={'session_id': session_id}
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_log_redirect_minimum_requirements(self, APIClientMock):
        hashid = 'aab32d8'
        redirection_id = 'ID'
        session_id = 'SESSION_ID'

        stats.log_redirect(hashid, redirection_id, session_id)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/redirect',
            query_params={
                'id': redirection_id,
                'session_id': session_id
            }
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_log_redirect(self, APIClientMock):
        hashid = 'aab32d8'
        redirection_id = 'ID'
        session_id = 'SESSION_ID'
        query = 'QUERY'

        stats.log_redirect(hashid, redirection_id, session_id, query)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/redirect',
            query_params={
                'id': redirection_id,
                'session_id': session_id,
                'query': query
            }
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_click_stats_minimum_requirements(self, APIClientMock):
        hashid = 'aab32d8'
        dfid = 'ID'
        session_id = 'SESSION_ID'

        stats.click_stats(hashid, dfid, session_id)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/click',
            query_params={
                'dfid': dfid,
                'session_id': session_id
            }
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_click_stats(self, APIClientMock):
        hashid = 'aab32d8'
        dfid = 'ID'
        session_id = 'SESSION_ID'
        query = 'QUERY'

        stats.click_stats(hashid, dfid, session_id, query)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/click',
            query_params={
                'dfid': dfid,
                'session_id': session_id,
                'query': query
            }
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_log_banner_image_click_minimum_requirements(self, APIClientMock):
        hashid = 'aab32d8'
        redirection_id = 'ID'
        session_id = 'SESSION_ID'

        stats.log_banner_image_click(hashid, redirection_id, session_id)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/image',
            query_params={
                'id': redirection_id,
                'session_id': session_id
            }
        )

    @mock.patch('pydoof.search_api.stats.SearchAPIClient')
    def test_log_banner_image_click(self, APIClientMock):
        hashid = 'aab32d8'
        redirection_id = 'ID'
        session_id = 'SESSION_ID'
        query = 'QUERY'

        stats.log_banner_image_click(hashid, redirection_id, session_id, query)

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/image',
            query_params={
                'id': redirection_id,
                'session_id': session_id,
                'query': query
            }
        )

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

        APIClientMock.return_value.put.assert_called_once_with(
            f'/6/{hashid}/stats/cart/{session_id}',
            query_params={
                'index': index_name, 'id': item_id, 'amount': amount,
                'title': title, 'price': price}
        )