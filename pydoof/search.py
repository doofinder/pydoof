import re

import requests

import pydoof

from pydoof.errors import handle_errors

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
                    for index, val in enumerate(params[key]):
                        if type(val) in (dict, list):
                            result.extend(cls.build_params_tuple(
                                val, '%s[%s]' % (newkey, index)))
                        else:
                            result.append(('%s[%s]' % (newkey, index), val))

                elif type(params[key]) is bool:
                    result.append((newkey, str(params[key]).lower()))
                else:
                    result.append((newkey, params[key]))
            return result
    
    @classmethod         
    def populate_headers(cls):
        """ Generates headers dict for search API
        request.

        Returns:
            a dictionary with necessary headers to make
            search requests.
        """

        headers = {}
        if pydoof.API_KEY:
            try:
                headers["API Token"] = (pydoof.API_KEY.split("-"))[1]

            except:
                pass
                
        return headers

    def search_api_call(self, hashid, query_term, page=1, filters=None,
                        query_name=None, **kwargs):
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
            any other keyword argument is passed as request parameter
            if keyword argument is array, is passed as repeated parameters

        Returns:
            A dict representing the response

        Raises:
            NotAllowed: if auth is failed.
            BadRequest: if the request is not proper
            WrongREsponse: if server error        
        """
        params = {}
        options = kwargs.pop('options', {})
        params.update(options)
        params = kwargs
        params.update({'hashid': hashid, 'query': query_term, 'page': page, 
                       'filter': filters,
                       'query_name': query_name})
        
        params = SearchApiClient.build_params_tuple(params)
        headers = SearchApiClient.populate_headers()
        
        response = requests.get(self.base_search_url, params=params, headers=headers)
        handle_errors(response)
        try:
            result =  {'status_code': response.status_code,
            'response': response.json() if response.text else {}}
        except ValueError:
            result =  {'status_code': response.status_code,
            'response': response.text}

        return result


    @property
    def base_search_url(self):
        """get base url for searching"""
        if not getattr(self, '_base_search_url', None):
            self._base_search_url = self.build_base_search_url()
        return self._base_search_url


    def build_base_search_url(self):
        """ Builds base url according to user-defined constants in pydoof"""
        if pydoof.API_KEY:
            cluster_region = pydoof.API_KEY.split('-')[0]
        elif pydoof.CLUSTER_REGION:
            cluster_region = pydoof.CLUSTER_REGION

        base_domain = pydoof.SEARCH_DOMAIN % cluster_region

        base_domain = re.sub('/?$', '', base_domain) # sanitize

        protocol = 'https' if pydoof.SEARCH_HTTPS else 'http'

        return '%s://%s/%s/search' % (protocol, base_domain,
                                      pydoof.SEARCH_VERSION)

            

        
