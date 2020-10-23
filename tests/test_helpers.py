from datetime import datetime
import unittest

from pydoof.helpers import parse_query_params


class TestParseQueryParams(unittest.TestCase):
    def test_can_parse_dates(self):
        """'Date' values can be parsed."""
        result = parse_query_params({
            'date': datetime(2020, 2, 12, 8, 32, 54)
        })

        self.assertEqual(result, {'date': '20200212'})

    def test_can_parse_dicts(self):
        """Dict values can be parsed."""
        result = parse_query_params({
            'dict0': {
                'dict1': {'a': 'a', 'b': 'b'},
                'list': [{'a': 'a'}, {'b': 'b'}],
                'string': 'String',
                'none': None
            }
        })

        self.assertEqual(
            result,
            {
                'dict0[dict1][a]': 'a',
                'dict0[dict1][b]': 'b',
                'dict0[list][][a]': 'a',
                'dict0[list][][b]': 'b',
                'dict0[string]': 'String'
            }
        )

    def test_can_parse_iterables(self):
        """Non-string iterables can be parsed."""
        result = parse_query_params({
            'iterable': ['a', 'b', 'c', 'd'],
            'string': 'String'
        })

        self.assertEqual(
            result,
            {'iterable[]': ['a', 'b', 'c', 'd'], 'string': 'String'}
        )

    def test_discards_none_values(self):
        """Parameters with 'None' values are discarded."""
        result = parse_query_params({
            'foo': True,
            'None': None,
            'bar': False
        })

        self.assertEqual(result, {'foo': True, 'bar': False})
