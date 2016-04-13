import re

import requests

import pydoof

from pydoof.errors import handle_errors

class MetaManagementApiClient(type):
    """
    Metaclass to add class properties accesor.

    The class is an std object for the metaclass
    """
    
    @property
    def base_management_url(cls):
        """get base_management_url according to pydoof constants"""        
        if not getattr(cls, '_base_management_url', None):
            management_version = pydoof.MANAGEMENT_VERSION
            management_domain = pydoof.MANAGEMENT_DOMAIN % cls.cluster_region
            management_domain = re.sub('/*$', '', management_domain) # sanitize
            cls._base_management_url = 'https://%s/v%s' % (management_domain,
                                                           management_version)
        #return 'http://localhost:8000/api/v1'
        return cls._base_management_url

    @property
    def cluster_region(cls):
        """get amazon cluster region by looking into API_KEY"""
        if not getattr(cls, '_cluster_region', None):
            cls._cluster_region, cls._token = pydoof.API_KEY.split('-')
        return cls._cluster_region

    @property
    def token(cls):
        """get auth token by looking into API_KEY"""
        if not getattr(cls, '_token', None):
            cls._cluster_region, cls._token = pydoof.API_KEY.split('-')
        return cls._token    


class ManagementApiClient(object):
    """Basic doofinder's api handling methods."""

    __metaclass__ = MetaManagementApiClient

    def __init__(self, **kwargs):
        super(ManagementApiClient, self).__init__(**kwargs)

    @classmethod
    def management_api_call(cls, method='get', entry_point='', params=None,
                            data=None):
        """
        Make the request and normalize response
        
        Args:
            method: The method to use. 'get', 'post', 'delete', 'put'
            entry_point: The entrypoint
            params: key-value dict of parameters to be sent in get request
            data: key-value data to be sent in a post request

        Returns:
            An object representing the response

        Raises:
            NotAllowed: if auth is failed.
            BadRequest: if the request is not proper
            WrongREsponse: if server error
        """

        assert(method in ['get', 'post', 'put', 'delete'])
        entry_point = re.sub('^/*(.*?)/*$', r'\1', entry_point) # sanitize
        headers = {'Authorization': 'Token %s' % cls.token,
                   'Content-Type': 'application/json'}
        do_request = getattr(requests, method)
        full_url = '%s/%s' % (cls.base_management_url, entry_point)
        r = do_request(full_url, headers=headers, params=params, data=data)

        handle_errors(r)
            
        try:
            return {'status_code': r.status_code,
                    'response': r.json() if r.text else {}}
        except ValueError as ve:
            return {'status_code': r.status_code,
                    'response': r.text}

    @classmethod
    def get_api_root(cls):
        """
        Obtain an object representing the management API root for this user.

        The API root contains entry points for managing

        Returns:
            dict
            Example:
                {<hashid>: {
                    'name': 'ktuin.com',
                    'items': {'product': <product crud entry point>},
                    'tasks': {
                        'process': <process task entry point>,
                        'crawl': <crawl task entry point>
                    }
                ....}
        """
        return cls.management_api_call()['response']




