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
                    for val in params[key]:
                        result.append(('%s[]' % newkey, val))
                elif type(params[key]) is bool:
                    result.append((newkey, str(params[key]).lower()))
                else:
                    result.append((newkey, params[key]))
            return result

    @classmethod
    def build_sorts_tuple(cls, params):
        """
        builds requests-understeandable sort params tuple

        Args:
            params: a list representing the sort parameters
                Example: [('brand': 'asc'), ('price': 'desc')]

        Returns:
            a list of sort-value tuples the requests lib can understand
            Example: [('sort[0][update_timestamp]','desc'), ('sort[1][name_sort]','asc')]
        """
        result = []
        for i, elem in enumerate(params):
            result.append(('sort[%s][%s]'%(i, elem[0]), elem[1]))

        return result


    def search_api_call(self, hashid, query_term, page=1, filters=None,
                        query_name=None, sort=None, **kwargs):
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
            sort: sort.
                Example:
                    [('brand': 'asc'),
                     ('price': 'desc')]
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

        if sort:
            params += SearchApiClient.build_sorts_tuple(sort)
        response = requests.get(self.base_search_url, params=params)
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

        base_domain = pydoof.SEARCH_DOMAIN.replace('%cluster_region%',
                                                   cluster_region)

        base_domain = re.sub('/?$', '', base_domain) # sanitize

        protocol = 'https' if pydoof.SEARCH_HTTPS else 'http'

        return '%s://%s/%s/search' % (protocol, base_domain,
                                      pydoof.SEARCH_VERSION)
