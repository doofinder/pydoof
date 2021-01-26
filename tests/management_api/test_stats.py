from parameterized import parameterized
from unittest import mock
import unittest

from pydoof.management_api.stats import (Devices, Formats, Sources, Types,
                                         banners, checkouts, clicks,
                                         clicked_items, clicked_items_searches,
                                         custom_results, facets, facets_top,
                                         inits, inits_locations,
                                         query_log_iter, redirects, sales,
                                         searches, searches_top, usage)


def _stats_test_cases():
    return [
        (banners,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'banner_id': '1235', 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/banners',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'id': '1235', 'tz': '+01:00', 'format': 'json'})),
        (checkouts,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'device': Devices.DESKTOP, 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/checkouts',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'tz': '+01:00', 'format': 'json'})),
        (clicks,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'device': Devices.DESKTOP, 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/clicks',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'tz': '+01:00', 'format': 'json'})),
        (clicked_items,
         {'query': 'QUERY', 'from_': '20200810', 'to': '20200910',
          'hashids': ['aab32d8'], 'device': Devices.DESKTOP, 'limit': 50,
          'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/clicked_items',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'query': 'QUERY', 'device': 'desktop', 'limit': 50, 'tz': '+01:00',
           'format': 'json'})),
        (clicked_items_searches,
         {'dfid': 'aab32d8@product@43ef82', 'from_': '20200810',
          'to': '20200910', 'hashids': ['aab32d8'], 'device': Devices.DESKTOP,
          'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/clicked_items/searches',
          {'from': '20200810', 'to': '20200910',
           'dfid': 'aab32d8@product@43ef82', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'tz': '+01:00', 'format': 'json'})),
        (custom_results,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'custom_result_id': '1235', 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/custom-results',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'id': '1235', 'tz': '+01:00', 'format': 'json'})),
        (facets,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/facets',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'tz': '+01:00', 'format': 'json'})),
        (facets_top,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/facets/top',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'tz': '+01:00', 'format': 'json'})),
        (inits,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'device': Devices.DESKTOP, 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/inits',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'tz': '+01:00', 'format': 'json'})),
        (inits_locations,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'device': Devices.DESKTOP, 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/inits/locations',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'tz': '+01:00', 'format': 'json'})),
        (redirects,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'redirect_id': '1235', 'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/redirects',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'id': '1235', 'tz': '+01:00', 'format': 'json'})),
        (sales,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'tz': '+01:00', 'format_': Formats.JSON},
         ('/api/v2/stats/sales',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'tz': '+01:00', 'format': 'json'})),
        (searches,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'device': Devices.DESKTOP, 'query_name': 'match_and',
          'source': Sources.VOICE, 'total_hits': 0, 'tz': '+01:00',
          'format_': Formats.JSON},
         ('/api/v2/stats/searches',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'query_name': 'match_and', 'source': 'voice',
           'total_hits': 0, 'tz': '+01:00', 'format': 'json'})),
        (searches_top,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'device': Devices.DESKTOP, 'query_name': 'match_and',
          'exclude': {'FIELD': 'VALUE'}, 'total_hits': 0, 'tz': '+01:00',
          'format_': Formats.JSON},
         ('/api/v2/stats/searches/top',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'device': 'desktop', 'query_name': 'match_and',
           'exclude[FIELD]': 'VALUE', 'total_hits': 0, 'tz': '+01:00',
           'format': 'json'})),
        (usage,
         {'from_': '20200810', 'to': '20200910', 'hashids': ['aab32d8'],
          'type_': Types.API, 'format_': Formats.JSON},
         ('/api/v2/stats/usage',
          {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8',
           'type': 'api_counters', 'format': 'json'})),
    ]


def _name_func(test_func, _num, param):
    stats_func = parameterized.to_safe_name(param.args[0].__name__)
    return f'{test_func.__name__}_{stats_func}'


def _docstring_func(_func, _num, param):
    stats_func = param.args[0]
    doc = f"Can request {stats_func.__name__} stats"
    return doc


class TestStats(unittest.TestCase):
    @parameterized.expand(_stats_test_cases,
                          name_func=_name_func,
                          doc_func=_docstring_func)
    @mock.patch('pydoof.management_api.stats.ManagementAPIClient')
    def test_stats(self, func, kwargs, expected_call, APIClientMock):
        func(**kwargs)
        APIClientMock.return_value.get.assert_called_with(*expected_call)

    @mock.patch('pydoof.management_api.stats.ManagementAPIClient')
    def test_stats_query_log_iter(self, APIClientMock):
        """Can stream query logs"""
        query_log_iter(from_='20200810', to='20200910', hashids=['aab32d8'])
        APIClientMock.assert_called_once_with(stream=True)
        APIClientMock.return_value.request.assert_called_with(
            'GET', '/api/v2/stats/query_log',
            {'from': '20200810', 'to': '20200910', 'hashid[]': 'aab32d8'}
        )
