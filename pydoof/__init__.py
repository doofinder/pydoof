import requests
import re

from pydoof.management import ManagementApiClient

API_KEY = None
"""
The API key to use when authenticating API requests.

The region must be included: token-region
Example: b42e3ea7c94c93555aa3dcdf2926ead136819518-eu1
"""

MANAGEMENT_DOMAIN = '%cluster_region%-api.doofinder.com'
""" The management API endpoint to send requests to."""

SEARCH_DOMAIN = '%cluster_region%-search.doofinder.com'
"""The search API endpoint to send search requests to"""

MANAGEMENT_VERSION = '1'
"""The version of server management API"""

SEARCH_VERSION = '4'
"""The version of server search API"""



class SearchEngine(ManagementApiClient):
    """
    SearchEngine's basic api management object

    - CRUD operations to search engine's indexed items
    - processing of the search engine's feeds
    """

    @classmethod
    def all(cls):
        """
        obtain search engines resources for this token

        Returns:
            A list of search engines.
        """
        search_engines = []

        for hashid, props in SearchEngine.get_api_root().iteritems():
            search_engines.append(SearchEngine(hashid, name=props['name'],
                                               datatypes=props['items'].keys()))
        return search_engines

    
    def __init__(self, hashid, name=None, datatypes=None):
        self.hashid = hashid 
        self.name = name
        self._datatypes = datatypes        


    def get_datatypes(self):
        """
        Get a list of searchengine's datatypes

        Returns:
            list of datatypes
            example:
            ['product', 'page']
        """
        
        if not self._datatypes and API_KEY:
            self._datatypes = [props['items'].keys() for hashid, props
                              in SearchEngine.get_api_root().iteritems()][0]
        return self._datatypes
        
    def get_items(self, item_type=None, page=1):
        """
        get paginated indexed items
        
        Args:
            item_type: the type of items . if none, use the first datatype
                        of the search engine
            page: the page number.

        Returns:
            array of dict representing items.
            example:
            [{'title': 'red shoes', 'price': 33.2}, {'title': 'blue shirt', 'price': 23.2}]
        """
        datatype = item_type if item_type else self.datatypes[0]
        
        result = SearchEngine.management_api_call(
            entry_point='%s/items/%s' % (self.hashid, datatype),
            params={'page': page})

        return result['response']['results']

    def get_item(self, item_type, id):
        """
        get details of a specific item
        Args:
            id: value of the identificator field of the item within its type
            item_type: type of the item.
                      if not provided, the search engine's first available datatype is used

        Returns:
            dict representing the item.
        """
        datatype = item_type if item_type else self.datatypes[0]

        return SearchEngine.management_api_call(
            entry_point='%s/items/%s/%s' % (self.hashid, datatype, id))['response']

    def add_item(self, item_description=None, item_type=None):
        """
        Add an item to the search engine

        Args:
            item_description: dict representing the item to be added
                NOTE: if item's id field not present, one will be created
            item_type: type of the item. If not provided, first one available
                       will be used

        Returns:
            the (id, datatype) typle of the created item , on success
        """
        datatype = item_type if item_type else self.datatypes[0]

        result = SearchEngine.management_api_call(
            'post', entry_point='%s/items/%s' % (self.hashid, datatype),
            data=item_description)

        return (self._obtain_id(result['response']['url']), datatype)

    def delete_item(self, id, item_type=None):
        """
        delete an item

        Args:
            id: item's unique identificator within its item_type
            item_type: if none the first available datatype is used

        Returns:
            true on success
        """
        datatype = item_type if item_type else self.datatypes[0]
        result = SearchEngine.management_api_call(
            'delete', entry_point='%s/items/%s/%s' % (self.hashid, datatype, id))

        if result['status_code'] == requests.codes.NO_CONTENT:
            return True
        else:
            return False

    def process(self):
        """
        Ask the server to process the search engine's feeds

        Returns:
            (True, task_id) The feed process has been started.
                            <task_id> is the id of the started process
            (False, task_id) There is another feed processing going on.
                             <task_id> is the id of the currently running process
        """
        result = SearchEngine.management_api_call(
            'post', entry_point='%s/tasks/process' % self.hashid)

        if result['status_code'] == requests.codes.CREATED:
            return (True, self._obtain_id(result['response']['link']))
        if result['status_code'] == request.codes.OK:
            return (False, self._obtain_id(result['response']['link']))

    def info(self, task_id):
        """
        Obtain info about how a process is going

        Returns:
            a dict with the keys 'state' and 'message'
            examples:
            - {'state': 'PROCESSING', 'message': 'Your task is being processed'}
            - {'state': 'SUCCESS', 'message': '1221 items processed'}
            - {'state': 'FAILURE', 'message': 'no data in the feed'}            
        """
        result = SearchEngine.management_api_call(
            entry_point='%s/tasks/%s' % (self.hashid, task_id))
        
        return result['response']

    def logs(self):
        """
        Obtain logs of the latest feed processing tasks done

        Returns:
            (list) list of dicts representing the logs
            example:[{'date': '2013-07-24T12:37:58.990', 
                     'level': 'ERROR', 
                     'msg': 'Wrong or not existent ...',
                     'log_type': 'log.parser'
                    }, {...}]
        """
        result = SearchEngine.management_api_call(
            entry_point='%s/tasks/process' % self.hashid)

        return result['response']
        


    def _obtain_id(self, url):
        """
        Extracs identifactor from an item or task url .

        Args:
            url: item or task resource locator

        Returns:
            the item or task identificator
        """
        url_re = re.compile('/(?P<hashid>\w{32})/(items/\w+)|(tasks)/(?P<id>[\w-]+)/?$')

        return url_re.search(url).groupdict()['id']
