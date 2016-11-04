# -*- coding: utf-8 -*-

import httpretty
import unittest
import pydoof
import json
import re

def request_callback(request, uri, headers):
    return (200, headers,
            json.dumps({'uri': uri, 'headers': request.headers.dict,
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
        self.assertIn('eu1-search', results['headers']['host'])
        # right path
        self.assertIn('/5/search', results['path'])
        # american api-token
        pydoof.API_KEY = 'us1-newtoken'
        results = pydoof.SearchEngine(self.hashid).query('test', 1)
        self.assertIn('us1-search', results['headers']['host'])
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


class TestManagementClient(unittest.TestCase):

    def setUp(self):
        pydoof.API_KEY = 'eu1-testtoken'
        self.hashid = 'ffffffffffffffffffffffffffffffff'
        self.hashid2 = 'fffffffffffffffffffffffffffffff2'
        self.se = pydoof.SearchEngine(self.hashid)
        self.items_url = "https://eu1-api.doofinder.com/v1/%s/items/product" % self.hashid

    @httpretty.activate
    def testHeadersZone(self):
        def test_headers_zone(request, uri, headers):
            rq_headers = request.headers.dict
            # right headers
            self.assertEqual(rq_headers['authorization'], 'Token testtoken')
            self.assertEqual(rq_headers['content-type'], 'application/json')
            # right zone
            self.assertIn('eu1-api', uri)
            return (200, headers, json.dumps({'searchengines': 'ok'}))

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        httpretty.register_uri(
            httpretty.GET, re.compile("https://(eu1|us1)-api.doofinder.com/v1/"),
            body=test_headers_zone)

        results = pydoof.SearchEngine.all()

    @httpretty.activate
    def testSearchEngineListing(self):

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        root_response = {
            "searchengines": "http://localhost:8000/api/v1/searchengines",
            "%s" % self.hashid: {
                "tasks": {"process": "ok"},
                "stats": { "aggregates": "ok"},
                "name": "account3.com",
                "items": { "estudio": "ok"},
                "types": "ok",
                "logs": "ok"
            },
            "%s" % self.hashid2: {
                "tasks": {"process": "ok"},
                "stats": {"aggregates": "ok"},
                "name": "really awesome",
                "items": {},
                "types": "ok",
                "logs": "ok"
            }
        }

        httpretty.register_uri(
            httpretty.GET, "https://eu1-api.doofinder.com/v1/",
            body=json.dumps(root_response))

        results = pydoof.SearchEngine.all()
        for res in results:
            self.assertEqual(type(res), pydoof.SearchEngine)
            self.assertEqual(res.name, root_response[res.hashid]['name'])

    @httpretty.activate
    def testSearchEngineTypesCrud(self):

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        se = pydoof.SearchEngine(self.hashid)
        types_url = "https://eu1-api.doofinder.com/v1/%s/types" % self.hashid

        # list types
        httpretty.register_uri(httpretty.GET, types_url,
                               body=json.dumps(['estudio', 'product']))

        self.assertListEqual(se.get_types(), ['estudio', 'product'])

        # add types
        httpretty.register_uri(httpretty.POST, types_url,
                               body=json.dumps(['product']))

        results = se.add_type('new_type')

        self.assertEqual(httpretty.last_request().method, 'POST')
        self.assertEqual(httpretty.last_request().body, json.dumps({'name': 'new_type'}))

        # delete type
        httpretty.register_uri(httpretty.DELETE, "%s/removeme" % types_url,
                               body=json.dumps(['product']))
        results = se.delete_type('removeme')
        self.assertEqual(httpretty.last_request().method, 'DELETE')

    @httpretty.activate
    def testSearchEngineItemsScroll(self):

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        total_results = [
                {"id": "id1", "title": "title1"},
                {"id": "id2", "title": "title2"},
                {"id": "id3", "title": "title3"},
                {"id": "id4", "title": "title4"},
                {"id": "id5", "title": "title5"},
                {"id": "id6", "title": "title6"}
            ]

        fake_response = {
            "next": "some url",
            "count": 6,
            "scroll_id": "test_scroll"
        }

        # scrolled items. three request to get them all
        # first request - standard : 3 results
        # second request - with scroll_id param: 3 results
        # third request - no results
        # we make a closure so we can count requests
        def make_closure():
            request_count = [0]
            def scrolled_items_request_callback(request, uri, headers):
                request_count[0] = request_count[0] + 1
                if request_count[0] == 1:
                    # no scroll id
                    self.assertFalse(request.querystring.has_key('scroll_id'))
                    fake_response['results'] = total_results[:3]
                    return(200, headers, json.dumps(fake_response))
                if request_count[0] == 2:
                    # scroll_id
                    self.assertEqual(request.querystring['scroll_id'][0], u'test_scroll')
                    fake_response['results'] = total_results[3:]
                if request_count[0] == 3:
                    self.assertEqual(request.querystring['scroll_id'][0], u'test_scroll')
                    fake_response['results'] = []
                return(200, headers, json.dumps(fake_response))

            return scrolled_items_request_callback

        # iterate all items
        httpretty.register_uri(httpretty.GET, self.items_url, body=make_closure())

        counter = 0
        for item in self.se.items('product'):
            self.assertEqual(item.id, total_results[counter]['id'])
            counter += 1

    @httpretty.activate
    def testSearchEngineItemsCrud(self):

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        # add item
        item1 = {
            "id":"id1",
            "t": "t1",
            "df_url": "/%s/items/product/id1" % self.hashid}

        httpretty.register_uri(httpretty.POST, self.items_url,
                               body=json.dumps(item1))

        result = self.se.add_item('product', item1)
        self.assertEqual(result, u'id1')
        self.assertEqual(httpretty.last_request().body, json.dumps(item1))

        # add items
        httpretty.reset()
        item2 = {
            "id":"id2",
            "t": "t2",
            "df_url": "/%s/items/product/id2" % self.hashid}

        httpretty.register_uri(httpretty.POST, self.items_url,
                               body=json.dumps([item1, item2]))

        result = self.se.add_items('product', [item1, item2])
        self.assertListEqual(result, [u'id1', u'id2'])
        self.assertEqual(httpretty.last_request().body, json.dumps([item1, item2]))

        # add/update items
        httpretty.reset()
        httpretty.register_uri(httpretty.PUT, self.items_url,
                               body=json.dumps([item1, item2]))

        self.assertTrue(self.se.update_items('product', [item1, item2]))
        self.assertEqual(httpretty.last_request().body, json.dumps([item1, item2]))


        # update item
        httpretty.register_uri(httpretty.PUT, '%s/id1' % self.items_url,
                               body=json.dumps(item1))

        self.assertTrue(self.se.update_item('product', 'id1', item1))
        self.assertEqual(httpretty.last_request().body, json.dumps(item1))

        # get item
        httpretty.register_uri(httpretty.GET, '%s/id1' % self.items_url,
                               body=json.dumps(item1))

        self.assertTrue(self.se.get_item('product', 'id1').id, 'id1')

        # delete item
        httpretty.register_uri(httpretty.DELETE, '%s/id1' % self.items_url,
                               body='', status=204)

        self.assertTrue(self.se.delete_item('product', 'id1'))
        self.assertEqual(httpretty.last_request().method, 'DELETE')


















if __name__ == '__main__':
    unittest.main()
