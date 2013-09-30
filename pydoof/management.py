import re

import requests

import pydoof

from pydoof.errors import handle_errors


class ManagementApiClient(object):
    """Basic doofinder's api handling methods."""

    def __init__(self, **kwargs):
        super(ManagementApiClient, self).__init__(**kwargs)

    def management_api_call(self, method='get', entry_point='', params=None,
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
        headers = {'Authorization': 'Token %s' % self.token,
                   'Content-Type': 'application/json'}
        do_request = getattr(requests, method)
        full_url = '%s/%s' % (self.base_management_url, entry_point)
        
        r = do_request(full_url, headers=headers, params=params, data=data)

        handle_errors(r)
            
        try:
            return {'status_code': r.status_code,
                    'response': r.json() if r.text else {}}
        except ValueError as ve:
            return {'status_code': r.status_code,
                    'response': r.text}


    def get_api_root(self):
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
        return self.management_api_call()['response']

    @property
    def base_management_url(self):
        """get base_management_url according to pydoof constants"""
        if not getattr(self, '_base_management_url', None):
            management_version = pydoof.MANAGEMENT_VERSION
            management_domain = pydoof.MANAGEMENT_DOMAIN.replace(
                '%cluster_region%', self.cluster_region)
            management_domain = re.sub('/*$', '', management_domain) # sanitize
            self._base_management_url = 'https://%s/v%s' % (management_domain,
                                                           management_version)
        return self._base_management_url

    @property
    def cluster_region(self):
        """get amazon cluster region by looking into API_KEY"""
        if not getattr(self, '_cluster_region', None):
            self._cluster_region, self._token = pydoof.API_KEY.split('-')
        return self._cluster_region

    @property
    def token(self):
        """get auth token by looking into API_KEY"""
        if not getattr(self, '_token', None):
            self._cluster_region, self._token = pydoof.API_KEY.split('-')
        return self._token
