# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
import datetime
import json
import re
import unittest

import httpretty
from requests.packages import urllib3

import pydoof
from pydoof.errors import NotProcessedResponse

# to disable sni warnings
urllib3.disable_warnings()


class TestManagementClient(unittest.TestCase):

    def setUp(self):
        pydoof.API_KEY = 'eu1-testtoken'
        self.hashid = 'ffffffffffffffffffffffffffffffff'
        self.hashid2 = 'fffffffffffffffffffffffffffffff2'
        self.se = pydoof.SearchEngine(self.hashid)
        self.items_url = "https://eu1-api.doofinder.com/v1/%s/items/product" % self.hashid
        self.stats_url = "https://eu1-api.doofinder.com/v1/%s/stats" % self.hashid
        self.tasks_url = "https://eu1-api.doofinder.com/v1/%s/tasks" % self.hashid
        self.logs_url = "https://eu1-api.doofinder.com/v1/%s/logs" % self.hashid

    @httpretty.activate
    def testHeadersZone(self):
        """ Test right auth and content-type headers are sent. Also right zone"""
        def test_headers_zone(request, uri, headers):
            rq_headers = request.headers
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
        self.assertEqual(httpretty.last_request().body.decode('utf-8'), json.dumps({'name': 'new_type'}))

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
                    self.assertFalse('scroll_id' in request.querystring)
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

        # iterate all items.
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
        self.assertEqual(httpretty.last_request().body.decode('utf-8'), json.dumps(item1))

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
        self.assertEqual(httpretty.last_request().body.decode('utf-8'), json.dumps([item1, item2]))

        # add/update items
        httpretty.reset()
        httpretty.register_uri(httpretty.PUT, self.items_url,
                               body=json.dumps([item1, item2]))

        self.assertTrue(self.se.update_items('product', [item1, item2]))
        self.assertEqual(httpretty.last_request().body.decode('utf-8'), json.dumps([item1, item2]))


        # update item
        httpretty.register_uri(httpretty.PUT, '%s/id1' % self.items_url,
                               body=json.dumps(item1))

        self.assertTrue(self.se.update_item('product', 'id1', item1))
        self.assertEqual(httpretty.last_request().body.decode('utf-8'), json.dumps(item1))

        # get item
        httpretty.register_uri(httpretty.GET, '%s/id1' % self.items_url,
                               body=json.dumps(item1))

        self.assertTrue(self.se.get_item('product', 'id1').id, 'id1')

        # delete item
        httpretty.register_uri(httpretty.DELETE, '%s/id1' % self.items_url,
                               body='', status=204)

        self.assertTrue(self.se.delete_item('product', 'id1'))
        self.assertEqual(httpretty.last_request().method, 'DELETE')

    @httpretty.activate
    def testStatsIteration(self):

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        full_aggs = [
                {
                    "date": "2016-10-20",
                    "searches": 11,
                    "requests": 33
                },
                {
                    "date": "2016-10-21",
                    "searches": 12,
                    "requests": 34
                },
                {
                    "date": "2016-10-22",
                    "searches": 11,
                    "requests": 33
                },
                {
                    "date": "2016-10-23",
                    "searches": 12,
                    "requests": 34
                }]

        fake_response={
            "start": "2016-10-20",
            "end": "2016-11-23",
            "count": 4,
            "next": None,
            "previous": None
        }

        # aggreates iteration.
        # first request- two first aggregates
        # second request - two last aggregates page = 2
        # third request - empty page = 3
        # we make a closure so we can count requests
        def make_closure():
            request_count = [0]
            def aggregates_iteration_request_callback(request, uri, headers):
                # always dates are present
                self.assertEqual(request.querystring['from'][0], u'20161020')
                self.assertEqual(request.querystring['to'][0], u'20161023')
                request_count[0] = request_count[0] + 1
                if request_count[0] == 1:
                    # page = 1
                    self.assertFalse('page' in request.querystring)
                    fake_response['aggregates'] = full_aggs[:2]
                if request_count[0] == 2:
                    self.assertEqual(request.querystring['page'][0], u'2')
                    fake_response['aggregates'] = full_aggs[2:]
                if request_count[0] == 3:
                    self.assertEqual(request.querystring['page'][0], u'3')
                    fake_response['aggregates'] = []
                return (200, headers, json.dumps(fake_response))
            return aggregates_iteration_request_callback

        from_date = datetime.datetime(2016,10,20)
        to_date = datetime.datetime(2016,10,23)

        # iterate all stats
        httpretty.register_uri(httpretty.GET, self.stats_url, body=make_closure())

        aggs = self.se.stats(from_date, to_date)

        counter = 0
        for ag in aggs:
            self.assertEqual(ag.searches, full_aggs[counter]['searches'])
            counter += 1

    @httpretty.activate
    def testTopTermsIteration(self):

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        fake_response = {
            "start": "2016-10-20",
            "end": "2016-11-03",
            "count": 3,
            "next": None,
            "previous": None
        }

        full_terms= {
            'searches': [
                {"term": 't1', 'count': 33},
                {"term": 't2', 'count': 34},
                {"term": 't3', 'count': 35}
            ],
            'opportunities': [
                {"term": 'op1', 'count': 33},
                {"term": 'op2', 'count': 34},
                {"term": 'op3', 'count': 35}
            ],
            'clicked': [
                {"term": 'red lightsaber', 'count': 33, 'url': 'http://example.com/1'},
                {"term": 'protocol', 'count': 34, 'url': 'http://example.com/2'},
                {"term": 'wwww', 'count': 35, 'url': 'http://example.com/3'}
            ]
        }


        # top terms iteration.
        # first request- two first searches
        # second request - one last search page = 2
        # third request - empty page = 3
        # we make a closure so we can count requests
        def make_closure(term_type='searches'):
            request_count = [0]
            def top_searches_iteration_request_callback(request, uri, headers):
                # always dates are present
                self.assertEqual(request.querystring['from'][0], u'20161020')
                self.assertEqual(request.querystring['to'][0], u'20161023')
                request_count[0] = request_count[0] + 1
                if request_count[0] == 1:
                    # page = 1
                    self.assertFalse('page' in request.querystring)
                    fake_response[term_type] = full_terms[term_type][:2]
                if request_count[0] == 2:
                    self.assertEqual(request.querystring['page'][0], u'2')
                    fake_response[term_type] = full_terms[term_type][2:]
                if request_count[0] == 3:
                    self.assertEqual(request.querystring['page'][0], u'3')
                    fake_response[term_type] = []
                return (200, headers, json.dumps(fake_response))
            return top_searches_iteration_request_callback


        from_date = datetime.datetime(2016,10,20)
        to_date = datetime.datetime(2016,10,23)

        for term_type in ('searches', 'opportunities', 'clicked'):

            # generation pending response
            httpretty.register_uri(httpretty.GET, '%s/top_%s' % (self.stats_url, term_type),
                                   status=202,
                                   body=json.dumps(
                                       {'url': 'xxx',
                                        'message': 'Your stats request is being processed.'
                                        ' Please check this url again later.'}
                                   )
            )
            with self.assertRaises(NotProcessedResponse) as cm:
                self.se.top_terms(term_type, from_date, to_date)

            httpretty.reset()

            # iterate all
            httpretty.register_uri(httpretty.GET, '%s/top_%s' % (self.stats_url, term_type),
                                   body=make_closure(term_type))

            counter = 0
            for search_term in self.se.top_terms(term_type, from_date, to_date):
                self.assertEqual(search_term.term, full_terms[term_type][counter]['term'])
                counter += 1
            self.assertEqual(counter, 3)

    @httpretty.activate
    def testTask(self):
        """ tests the process task"""

        httpretty.HTTPretty.allow_net_connect = False # don't allow outside net access

        # task not accepted response
        httpretty.register_uri(httpretty.POST, '%s/process' % self.tasks_url, status=200, body='')

        self.assertEqual(self.se.process(), (False, None))

        httpretty.reset()
        # task accepted response
        httpretty.register_uri(httpretty.POST, '%s/process' % self.tasks_url, status=201,
                               body=json.dumps({'link': '%s/task_id' % self.tasks_url}))

        self.assertEqual(self.se.process(), (True, 'task_id'))

        fake_response = {
            "state": "SUCCESS",
            "message": "ok",
            "task_name": "process"
        }

        # process info
        httpretty.register_uri(httpretty.GET, '%s/process' % self.tasks_url, status=200,
                               body=json.dumps(fake_response))

        self.assertDictEqual(self.se.process_info(),
                             {'state': 'SUCCESS', 'message': 'ok'})

    @httpretty.activate
    def testLogs(self):
        """ test log retrieval"""

        fake_logs = [
            {
                "date": "2016-11-07T18:12:19.688329Z",
                "level": "INFO",
                "msg": "Feed product Processed Successfully. Items:24 / Size:78Kb"
            },
            {
                "date": "2016-11-07T18:10:08.130279Z",
                "level": "INFO",
                "msg": "Feed product Processed Successfully. Items:24 / Size:78Kb"
            },
            {
                "date": "2016-11-07T18:07:57.920452Z",
                "level": "INFO",
                "msg": "Feed product Processed Successfully. Items:24 / Size:78Kb"
            }
        ]
        httpretty.register_uri(httpretty.GET, self.logs_url,
                               body=json.dumps(fake_logs))

        self.assertListEqual(fake_logs, self.se.logs())
