import re

import requests

import pydoof

from pydoof.errors import NotAllowed, BadRequest


class ManagementApiClient(object):
    """
    Basic doofinder's api handling methods.

    - holder of api entrypoints
    - communication with server
    - holder of auth token
    """

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
            WrongRequest: if it can't understand the response
        """

        assert(method in ['get', 'post', 'put', 'delete'])
        # ensamble settings
        token, cluster_region = pydoof.API_KEY.split('-')
        base_url = pydoof.MANAGEMENT_DOMAIN.replace('%cluster_region%', cluster_region)
        # sanitize entry point
        entry_point = re.sub('^/*(.*?)/*$', r'\1', entry_point) 
        headers = {'Authorization': 'Token %s' % token}
        do_request = getattr(requests, method)
        full_url = 'http://%s/v%s/%s' % (base_url, pydoof.MANAGEMENT_VERSION,
                                         entry_point)
        r = do_request(full_url, headers=headers, params=params, data=data)

        if r.status_code == requests.codes.FORBIDDEN:
            raise NotAllowed("The user does not have permissions to "
                             "perform this operation")
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
