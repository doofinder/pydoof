"""
Common classes for Management and Search modules.
"""
import requests
try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

import pydoof


class PyDoofError(Exception):
    """Generic Doofinder API Error."""


class APIConnectionError(PyDoofError):
    """
    Generic Error while processing HTTP Requests.

    These are not errors coming from Doofinder. But for instance, errors
    establishing the connection or parsing the response.
    """
    def __init__(self, message=None, original_exc=None):
        self.message = message
        self.original_exc = original_exc

    def __str__(self):
        error_message = []
        if self.message:
            error_message += [f"{self.message}"]
        if self.original_exc:
            error_message += [f"{type(self.original_exc).__name__}"]
            if str(self.original_exc):
                error_message += [f": {str(self.original_exc)}"]
        return "\n".join(error_message)


class DoofinderAuth(requests.auth.AuthBase):
    """Authenticator for Doofinder APIs."""
    def __init__(self, token=None, dfmaster_token=None):
        self.token = token
        self.dfmaster_token = dfmaster_token

    def __call__(self, r):
        if self.token is not None:
            r.headers['Authorization'] = f'Token {self.token}'
        if self.dfmaster_token is not None:
            r.headers['dfmastertoken'] = self.dfmaster_token
        return r


class APIClient():
    """
    Base Doofinder API Client.

    Includes methods for basic requests to a Doofinder endpoints. You should
    not use this class, but create an API Client that inherit from it. The
    child API Client should implement `_handle_response_error`. That method
    takes the response error and raises the corresponding exception.
    """
    ALLOWED_REQUEST_OPTS = ('allow_redirects', 'cert', 'proxies', 'stream',
                            'timeout', 'verify')

    def __init__(self, **kwargs):
        dfmaster_token = (
            kwargs.get('_dfmaster_token') or pydoof._dfmaster_token
        )
        token = kwargs.get('token') or pydoof.token

        self.authentication = DoofinderAuth(
            token=token, dfmaster_token=dfmaster_token
        )
        self.headers = {'User-Agent': 'doofinder-api-client/python'}
        self.request_opts = {
            k: v for k, v in kwargs.items() if k in self.ALLOWED_REQUEST_OPTS
        }
        self.session = requests.Session()

    def request(self, method, url, query_params=None, json=None):
        try:
            response = self.session.request(
                method,
                url=f'{self.host}{url}',
                params=query_params,
                json=json,
                headers=self.headers,
                auth=self.authentication,
                **self.request_opts
            )
        except Exception as exc:
            raise APIConnectionError(
                message="Unexpected error communicating with Doofinder.",
                original_exc=exc
            )

        if not 200 <= response.status_code < 300:
            err = self._handle_response_error(response)
            raise err

        if self.request_opts.get('stream', False):
            response_body = response.iter_content(chunk_size=None)
        else:
            try:
                response_body = response.json()
            except JSONDecodeError:
                response_body = response.text
        return response_body

    def get(self, url, query_params=None):
        return self.request('GET', url, query_params)

    def delete(self, url, query_params=None):
        return self.request('DELETE', url, query_params)

    def post(self, url, json=None, query_params=None):
        return self.request('POST', url, query_params, json)

    def patch(self, url, json=None, query_params=None):
        return self.request('PATCH', url, query_params, json)
