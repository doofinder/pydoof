import re

import requests

import pydoof

from pydoof.errors import BadRequest, WrongResponse

class SearchApiClient(object):
    """Basic doofinder's api search methods"""

    def __init__(self, **kwargs):
        super(SearchApiClient, self).__init__(**kwargs)


    @classmethod
    def build_params_tuple(cls, params, topkey=''):
        """
        builds requests-understeandable params tuple

        Args:
            params: a complex python nested dict representing a data structure
                Example: {'terms':{'color':['blue', 'red']}}

        Returns:
            a list of param-value tuples the requests lib can understand
            Example: [('terms[color][]', 'blue'), ('terms[color][]', 'red')]
        """
 
        if len(params) == 0:
            return []
 
        result = []
 
        # is a dictionary?
        if type (params) is dict:
            for key in params.keys():
                newkey = key
                if topkey != '':
                    newkey = '%s[%s]' % (topkey, key)
 
                if type(params[key]) is dict:
                    result.extend(cls.build_params_tuple(params[key], newkey))
 
                elif type(params[key]) is list:
                    for val in params[key]:
                        result.append(('%s[]' % newkey, val))
                elif type(params[key]) is bool:
                    result.append((newkey, str(params[key]).lower()))
                else:
                    result.append((newkey, params[key]))
            return result
                

    def search_api_call(self, hashid, query_term, page=1, filters=None,
                        query_name=None):
        """
        make the request and return dict representing response

        Args:
            query_term:  the actual query
            page: page number
            filters: filter definition.
                Example:
                    {'brand': ['nike', 'addidas'],
                    'price': {'from': 2.34, 'to': 12}}
            query_name: instructs doofinder to use only that query type

        Returns:
            A dict representing the response
        """
        params = SearchApiClient.build_params_tuple(
            {'hashid': hashid, 'query': query_term, 'page': page,
             'filter': self.build_ES_filters(filters)})
        result = requests.get(self.base_search_url, params=params)
        return result

    @classmethod
    def build_ES_filters(cls, filters):
        """
        Translate SearchEngine friendly filter format
        {'color': ['blue', 'red'], 'price': {'from':33}}
        to a dict representing elasticsearch friendly format
        {'terms': {'color': ['blue', 'red']},
        'numeric_range': {'price': {'from': 33}}

        Args:
            filters: dict with filters definition as in make_search_api

        Returns:
            querystring  with the elastic search filters format
        """
        if not filters:
            return None
        terms = {}
        numeric_range = {}
        result = {}
        for key, definition in filters.iteritems():
            if type(definition) == list: # terms
                terms[key] = definition
            if type(definition) == dict:
                numeric_range[key] = definition
        if terms:
            result['terms'] = terms
        if numeric_range:
            result['numeric_range'] = numeric_range

        return result

    @property
    def base_search_url(self):
        if not getattr(self, '_base_search_url', None):
            self._base_search_url = self.build_base_search_url()
        return self._base_search_url


    def build_base_search_url(self):
        """ Builds base url according to user-defined constants in pydoof"""
        if pydoof.API_KEY:
            cluster_region = pydoof.API_KEY.split('-')[1]
        elif pydoof.CLUSTER_REGION:
            cluster_region = pydoof.CLUSTER_REGION

        base_domain = pydoof.SEARCH_DOMAIN.replace('%cluster_region%',
                                                   cluster_region)

        base_domain = re.sub('/?$', '', base_domain) # sanitize

        protocol = 'https' if pydoof.HTTPS else 'http'

        return '%s://%s/%s/search' % (protocol, base_domain,
                                      pydoof.SEARCH_VERSION)

            

        
