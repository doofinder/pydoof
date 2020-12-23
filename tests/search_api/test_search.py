from unittest import mock
import unittest

from pydoof.search_api.search import QueryNames, Transformers, query, suggest


class TestSearch(unittest.TestCase):

    @mock.patch('pydoof.search_api.search.SearchAPIClient')
    def test_query(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        page = 1
        rpp = 10

        query(
            hashid, 'QUERY', filter_={'color': 'red'},
            exclude={'color': 'blue'}, index_name=index_name,
            query_name=QueryNames.MATCH_AND, sort=[{'brand': 'asc'}],
            page=page, rpp=rpp, transformer=Transformers.ONLY_IDS,
            no_stats=True
        )

        APIClientMock.return_value.get.assert_called_once_with(
            '/5/search',
            query_params={'hashid': hashid, 'query': 'QUERY',
                          'filter[color]': 'red',
                          'exclude[color]': 'blue',
                          'type': 'product',
                          'query_name': 'match_and',
                          'sort[][brand]': 'asc',
                          'page': page, 'rpp': rpp,
                          'transformer': 'onlyid',
                          'nostats': True}
        )

    @mock.patch('pydoof.search_api.search.SearchAPIClient')
    def test_sugges(self, APIClientMock):
        hashid = 'aab32d8'
        page = 1
        rpp = 10

        suggest(
            hashid, 'QUERY', filter_={'color': 'red'},
            exclude={'color': 'blue'}, sort=[{'brand': 'asc'}],
            page=page, rpp=rpp, transformer=Transformers.BASIC, no_stats=True
        )

        APIClientMock.return_value.get.assert_called_once_with(
            '/5/suggest',
            query_params={'hashid': hashid, 'query': 'QUERY',
                          'filter[color]': 'red',
                          'exclude[color]': 'blue',
                          'sort[][brand]': 'asc',
                          'page': page,
                          'rpp': rpp,
                          'transformer': 'basic',
                          'nostats': True}
        )
