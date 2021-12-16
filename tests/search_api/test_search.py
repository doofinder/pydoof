from unittest import mock
import unittest

from requests.sessions import session

from pydoof.search_api.search import query, suggest

from pydoof.search_api.enums import QueryNames


class TestSearch(unittest.TestCase):

    @mock.patch('pydoof.search_api.search.SearchAPIClient')
    def test_minimum_requirements_query(self, APIClientMock):
        hashid = 'aab32d8'

        query(hashid, 'QUERY')

        APIClientMock.return_value.get.assert_called_once_with(
            f'/6/{hashid}/_search',
            query_params={'hashid': hashid, 'query': 'QUERY'}
        )

    @mock.patch('pydoof.search_api.search.SearchAPIClient')
    def test_query(self, APIClientMock):
        hashid = 'aab32d8'
        indices = ['product', 'another_index']
        facets = [{'field': 'brand', 'size': 10}, {'field': 'price'}]
        session_id = 'SESSION_ID'
        skip_to_facet = ['TOP_FACET0', 'TOP_FACET1']
        skip_auto_filters = ['AUTO_FILTER0', 'AUTO_FILTER1']
        page = 1
        rpp = 10

        query(
            hashid, 'QUERY', filter={'brand': 'MyBrand'},
            exclude={'color': ['blue', 'red'], 'size': 'M',
                     'price': {'gte': 4.36, 'lt': 99}},
            facets=facets, session_id=session_id, indices=indices, query_name=QueryNames.MATCH_AND,
            sort=[{'brand': 'asc'}], page=page, rpp=rpp, stats=True, skip_top_facet=skip_to_facet,
            skip_auto_filters=skip_auto_filters
        )

        APIClientMock.return_value.get.assert_called_once_with(
            f'/6/{hashid}/_search',
            query_params={'hashid': hashid, 'query': 'QUERY',
                          'filter[brand]': 'MyBrand',
                          'exclude[color][]': ['blue', 'red'],
                          'exclude[size]': 'M',
                          'exclude[price][gte]': 4.36,
                          'exclude[price][lt]': 99,
                          'facets[0][field]': 'brand',
                          'facets[0][size]': 10,
                          'facets[1][field]': 'price',
                          'indices[]': indices,
                          'session_id': session_id,
                          'query_name': 'match_and',
                          'sort[][brand]': 'asc',
                          'page': page, 'rpp': rpp,
                          'stats': True,
                          'skip_top_facet[]': skip_to_facet,
                          'skip_auto_filters[]': skip_auto_filters}
        )

    @mock.patch('pydoof.search_api.search.SearchAPIClient')
    def test_suggest(self, APIClientMock):
        hashid = 'aab32d8'
        indices = ['product', 'another_index']
        suggest(
            hashid, 'QUERY', indices, stats=False
        )

        APIClientMock.return_value.get.assert_called_once_with(
            f'/6/{hashid}/_suggest',
            query_params={'query': 'QUERY',
                          'indices[]': indices,
                          'stats': False}
        )
