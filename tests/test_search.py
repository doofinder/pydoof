# -*- coding: utf-8 -*-

import httpretty
import unittest
import pydoof
import json
import re


from requests.packages import urllib3

# to disable sni warnings
urllib3.disable_warnings()

def request_callback(request, uri, headers):
    return (200, headers,
            json.dumps({'uri': uri, 'headers': dict(request.headers),
                        'parameters': request.querystring, 'path': request.path}))


class TestSearchClient(unittest.TestCase):

    def setUp(self):
        pydoof.API_KEY = 'eu1-testtoken'
        self.hashid = 'ffffffffffffffffffffffffffffffff'
        self.se = pydoof.SearchEngine(self.hashid)


    @httpretty.activate
    def testPathZoneToken(self):
        """ test requests are authenticated and to the right zone and has the right path"""
        httpretty.HTTPretty.allow_net_connect = False # raise error if trying to access other uri
        # european api-token
        httpretty.register_uri(
            httpretty.GET, re.compile("https://(eu1|us1)-search.doofinder.com/(4|5)/([\w/+])"),
            body=request_callback)
        results = self.se.query('test', 1)
        # right authtoken
        self.assertEqual(results['headers']['authorization'], u'testtoken')
        # right zone
        if 'Host' in results['headers']:
            self.assertIn('eu1-search', results['headers']['Host'])

        else:
            self.assertIn('eu1-search', results['headers']['host'])
        # right path
        self.assertIn('/5/search', results['path'])
        # american api-token
        pydoof.API_KEY = 'us1-newtoken'
        results = pydoof.SearchEngine(self.hashid).query('test', 1)
        self.assertIn('us1-search', results['headers']['Host'])
        self.assertEqual(results['headers']['authorization'], u'newtoken')

        # if not token, not allowed
        pydoof.API_KEY = None
        with self.assertRaises(pydoof.errors.Unauthorized) as m:
            pydoof.SearchEngine(self.hashid).query('test', 1)

    @httpretty.activate
    def testOptions(self):
        """ test options retrieval from server """
        httpretty.HTTPretty.allow_net_connect = False # raise error if trying to access other uri
        options = { 'optiona': 'valuea', 'optionb': {'suba': 'va', 'subb': 'vb'}}

        httpretty.register_uri(
            httpretty.GET, "https://eu1-search.doofinder.com/5/options/{}".format(self.hashid),
            body=request_callback)

        result = self.se.get_options()
        self.assertEqual(
            result['uri'],
            u'https://eu1-search.doofinder.com/5/options/%s' % self.hashid)


    @httpretty.activate
    def testSearchParams(self):
        """ test basic search capabilities"""
        httpretty.HTTPretty.allow_net_connect = False # raise error if trying to access other uri

        httpretty.register_uri(
            httpretty.GET, re.compile("https://eu1-search.doofinder.com/5/search"),
            body=request_callback)

        # Making queries with filters and a specific query_name
        results = self.se.query('test query', 3,
                                {
                                    'brand': ['nike', 'asics'],
                                    'price': {'gte': 2.45, 'lt': 100}
                                },
                                'match_and'  # the query_name
                            )
        # all parameters in place
        self.assertDictEqual({
            'filter[price][lt]': [u'100'], 'filter[price][gte]': [u'2.45'],
            'filter[brand][0]': [u'nike'], 'filter[brand][1]': [u'asics'],
            'query_name': [u'match_and'], 'hashid': [self.hashid], 'query': [u'test query'],
            'page': [u'3']}, results['parameters'])

        # any keyword arg is passed as parameter
        results = self.se.query('test query', rpp=12, lang='pt', transformer='dflayer')
        self.assertDictContainsSubset(
            {'query': [u'test query'], 'rpp': [u'12'], 'transformer': [u'dflayer']},
            results['parameters'])

        # Use of the sort parameter
        results = self.se.query(
            query_term='test query',
            sort= [{'namet':'asc'}, {'update_timestamp': 'desc'}])

        self.assertDictContainsSubset(
            {'sort[0][namet]': [u'asc'], 'sort[1][update_timestamp]': [u'desc']},
            results['parameters'])

    @httpretty.activate
    def testSearchResults(self):
        """ test results handling """
        httpretty.HTTPretty.allow_net_connect = False # raise error if trying to access other uri

        fake_response = {
            "query_counter": 1,
            "results_per_page": 3,
            "page": 1,
            "total": 3,
            "query": "silla",
            "hashid": "6a96504dc173514cab1e0198af92e6e9",
            "max_score": 0.702,
            "results": [
                {
                    "id": "id1",
                    "title": "Vigilabebés digital hume y vibración",
                },
                {
                    "id": "AOX11302",
                    "title": "Colchoneta reversible maclaren gold - black",
                },
                {
                    "id": "AVESCD52000",
                    "title": "Vigilabebés digital recargable con lcd temp y nanas",
                }
            ],
            "query_name": "phonetic_text",
            "facets": {
                "best_price": { "range": "ok"},
                "categories": { "terms": "ok"}
            }
        }


        httpretty.register_uri(
            httpretty.GET, "https://eu1-search.doofinder.com/5/search",
            body=json.dumps(fake_response))

        results = self.se.query('test query')
        self.assertEqual(results.total, 3)
        self.assertEqual(results.max_score, 0.702)
        self.assertEqual(results.query_name, 'phonetic_text')
        self.assertDictEqual(
            results.facets,
            {'best_price': {'range': 'ok'}, 'categories': {'terms': 'ok'}}
        )

        res = results.get_items()
        self.assertEqual(len(res), 3)
        self.assertEqual(res[1]['id'], u'AOX11302')
