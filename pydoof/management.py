import re

import requests

import pydoof

from pydoof.errors import NotAllowed, BadRequest, WrongResponse


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
            BadRequest: if it can't understand the response
        """

        assert(method in ['get', 'post', 'put', 'delete'])
        entry_point = re.sub('^/*(.*?)/*$', r'\1', entry_point) # sanitize
        headers = {'Authorization': 'Token %s' % self.token,
                   'Content-Type': 'application/json'}
        do_request = getattr(requests, method)
        full_url = '%s/%s' % (self.base_management_url, entry_point)
        
        r = do_request(full_url, headers=headers, params=params, data=data)

        if r.status_code == requests.codes.FORBIDDEN:
            raise NotAllowed("The user does not have permissions to "
                             "perform this operation")
        if r.status_code == requests.codes.UNAUTHORIZED:
            raise NotAllowed("The user hasn't provided valid authorization")
        if r.status_code == requests.codes.NOT_FOUND:
            raise BadRequest("%s Not Found" % full_url)
        if r.status_code == requests.codes.CONFLICT:
            raise BadRequest("Request conflict")
        if r.status_code > 400 and r.status_code < 500:
            raise BadRequest('The client made a bad request')
            
        try:
            return {
                'status_code': r.status_code,
                'response': r.json() if r.text else {}
                }
        except ValueError as ve:
            raise WrongResponse(ve)


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
        if not getattr(self, '_base_management_url', None):
            management_version = pydoof.MANAGEMENT_VERSION
            management_domain = pydoof.MANAGEMENT_DOMAIN.replace(
                '%cluster_region%', self.cluster_region)
            management_domain = re.sub('/*$', '', management_domain) # sanitize
            self._base_management_url = 'http://%s/v%s' % (management_domain,
                                                           management_version)
        return self._base_management_url

    @property
    def cluster_region(self):
        if not getattr(self, '_cluster_region', None):
            self._token, self._cluster_region = pydoof.API_KEY.split('-')
        return self._cluster_region

    @property
    def token(self):
        if not getattr(self, '_token', None):
            self._token, self._cluster_region = pydoof.API_KEY.split('-')
        return self._token
