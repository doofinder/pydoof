# -*- coding: utf-8 -*-

import re

import requests

class NotAllowed(Exception):
    """ raised when auth fails"""
    pass

class WrongResponse(Exception):
    """ raised when response can't be parsed"""
    pass

class BadRequest(Exception):
    """ raised when the client makes a bad request"""
    pass

class ApiClient(object):
    """
    Basic doofinder's api handling methods.

    - holder of api entrypoints
    - communication with server
    - holder of auth token
    """

    def __init__(self, token, url='http://www.doofinder.com/api', version='1'):
        """
        Args:
            token: user's auth token
            url: Basic api entrypoint
            version: version of the api to use
        """
        assert(token)
        self.token = token
        # sanitize everything. non slashes at start or end
        self.url = re.sub('/*$', '', url) 
        self.version = re.sub('^/*(.*?)/*$', r'\1',version)

    def make_api_call(self, method='get', entry_point='', params=None, data=None):
        """
        Make the request and normalize response
        
        Args:
            method: The method to use. 'get', 'post', 'delete', 'put'
            entry_point: The entrypoint
            params: key-value dict of parameters

        Returns:
            An object representing the response

        Raises:
            NotAllowed: if auth is failed.
            WrongRequest: if it can't understand the response
        """
        assert(method in ['get', 'post', 'put', 'delete'])
        entry_point = re.sub('^/*(.*?)/*$', r'\1', entry_point) # sanitize entry point
        headers = {'Authorization': 'Token %s' % self.token}
        do_request = getattr(requests, method)
        full_url = '%s/v%s/%s' % (self.url, self.version, entry_point)
        r = do_request(full_url, headers=headers, params=params, data=data)

        if r.status_code == requests.codes.FORBIDDEN:
            raise NotAllowed("The user does not have permissions to perform this operation")
        if r.status_code == requests.codes.UNAUTHORIZED:
            raise NotAllowed("The user hasn't provided valid authorization")
        if r.status_code == requests.codes.NOT_FOUND:
            raise BadRequest("%s Not Found" % full_url)
        if r.status_code > 400 and r.status_code < 500:
            raise BadRequest('The client made a bad request')
            
        try:
            return {
                'status_code': r.status_code,
                'response': r.json() if r.text else {}
                }
        except ValueError as ve:
            raise WrongResponse(ve)


    
        
def search_engines(token, url=None, version=None):
    """ obtain search engines resources for this token

    Args:
        token: user's auth token
        url: Basic api entrypoint
        version: version of the api to use

    Returns:
        A dict mapping search_engine's names and object
        example:
            {'ktuin.com': <SearchEngine>}
    """
    kwargs = {}
    search_engines = {}
    if url:
        kwargs['url'] = url
    if version:
        kwargs['version'] = version

    client = ApiClient(token, **kwargs)

    response = client.make_api_call()['response']

    for hashid in response:
        kwargs['datatypes'] = response[hashid]['items'].keys()
        search_engines[response[hashid]['name']] = SearchEngine(hashid, token,
                                                                response[hashid]['name'], **kwargs)
    return search_engines

def _obtain_datatypes(hashid, token, url=None, version=None):
    """ obtain datatypes associated with a hashid
    Args:
        token: user's auth token
        url: basic api entrypoint
        version: version of the api to use
    Returns:
        datatypes array
    """
    kwargs={}
    if url:
        kwargs['url'] = url
    if version:
        kwargs['version'] = version

    client = ApiClient(token, **kwargs)
    result = client.make_api_call()

    return result['response'].get(hashid, {'items': []})['items'].keys()


class SearchEngine(ApiClient):
    """
    SearchEngine's api management object

    - CRUD operations to search engine's indexed items
    - processing of the search engine's feeds
    """

    def __init__(self, hashid, token, name, datatypes=None, **kwargs):
        super(SearchEngine, self).__init__(token, **kwargs)
        self.hashid = hashid 
        self.name = name 
        if not datatypes:
            self.datatypes = _obtain_datatypes(hashid, token, **kwargs)
        else:
            self.datatypes = datatypes

        self.last_processing_state = None # last processing task state received
        self.last_processing_message = None # last processing task message received


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
        
        result = self.make_api_call(entry_point='%s/%s' % (self.hashid, datatype), params={'page': page})
        return result['response']['results']

    def get_item(self, id, item_type=None):
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
        return self.make_api_call(entry_point='%s/%s/%s' % (self.hashid, datatype, id))['response']

    def add_item(self, item_description=None, item_type=None):
        """
        Add an item to the search engine

        Args:
            item_description: dict representing the item to be added
                              NOTE: if item's id field not present, one will be dynamically created
            item_type: type of the item. If not provided, first one available will be used

        Returns:
            the (id, datatype) typle of the created item , on success
        """
        datatype = item_type if item_type else self.datatypes[0]
        result = self.make_api_call(method='post', entry_point='%s/%s' % (self.hashid, datatype),
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
        result = self.make_api_call(method='delete', entry_point='%s/%s/%s' % (self.hashid, datatype, id))
        if result['status_code'] == requests.codes.NO_CONTENT:
            return True

    def process_feeds(self):
        """
        Ask the server to process the search engine's feeds

        Returns:
            (True, task_id) The feed process has been started.
                            <task_id> is the id of the started process
            (False, task_id) There is another feed processing going on.
                             <task_id> is the id of the currently running process
        """
        result = self.make_api_call(method='post', entry_point='%s/process_tasks' % self.hashid)
        if result['status_code'] == requests.codes.CREATED:
            return (True, self._obtain_id(result['response']['link']))
        if result['status_code'] == request.codes.OK:
            return (False, self._obtain_id(result['response']['link']))

    def get_processing_info(self, task_id):
        """
        Obtain info about how a process is going

        Also, updates 'last_processing_state' and 'last_processing_message' attribures

        Returns:
            a dict with the keys 'state' and 'message'
            examples:
            - {'state': 'PROCESSING', 'message': 'Your task is being processed'}
            - {'state': 'SUCCESS', 'message': '1221 items processed'}
            - {'state': 'FAILURE', 'message': 'no data in the feed'}            
        """
        result = self.make_api_call(entry_point= '%s/process_tasks/%s' % (self.hashid, task_id))
        self.last_processing_state = result['response']['state']
        self.last_processing_message = result['response']['message']
        
        return result['response']

    def get_processing_logs(self):
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
        result = self.make_api_call(entry_point='%s/process_tasks' % self.hashid)
        return result['response']
        


    def _obtain_id(self, url):
        """
        Extracs identifactor from an item or task url .

        Args:
            url: item or task resource locator

        Returns:
            the item or task identificator
        """
        url_re = re.compile('/(?P<hashid>\w{32})/(\w+)/(?P<id>[\w]+)/?$')

        return url_re.search(url).groupdict()['id']

        
        
            
        
                
        
        


        
        


    

