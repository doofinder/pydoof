"""
"""
import requests
try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

import pydoof_beta


class PyDoofError(Exception):
    """Generic PyDoof Error"""
    pass


class APIConnectionError(PyDoofError):
    """"""
    def __init__(self, message=None, original_exc=None):
        self.message = message
        self.original_exc = original_exc

    def __str__(self):
        error_message = "\n"
        if self.message:
            error_message += f"{self.message}\n\n"
        if self.original_exc:
            error_message += f"{type(self.original_exc).__name__}"
            if str(self.original_exc):
                error_message += f": {str(self.original_exc)}"
        return error_message


class DoofinderAuth(requests.auth.AuthBase):
    def __init__(self, token=None, dfmaster_token=None):
        self.token = token
        self.dfmaster_token = dfmaster_token

    def __call__(self, r):
        if self.token is not None:
            r.headers['Authorization'] = f'Token {self.token}'
        if self.dfmaster_token is not None:
            r.headers['dfmastertoken'] = self.dfmaster_token
        return r


class ApiClient():
    """
    """
    def __init__(self, **kwargs):
        self.headers = {'User-Agent': 'doofinder-api-client/python'}
        self.dfmaster_token = (
            kwargs.get('_dfmaster_token') or pydoof_beta._dfmaster_token
        )
        self.token = kwargs.get('token') or pydoof_beta.token

    @property
    def authentication(self):
        return DoofinderAuth(token=self.token,
                             dfmaster_token=self.dfmaster_token)

    def request(self, method, url, query_params=None, json=None,
                **request_opts):
        print(query_params)
        try:
            response = requests.request(
                method,
                url=f'{self.host}{url}',
                params=query_params,
                json=json,
                headers=self.headers,
                auth=self.authentication,
                **request_opts
            )
        except Exception as exc:
            raise APIConnectionError(
                message="Unexpected error communicating with Doofinder.",
                original_exc=exc
            )

        if not 200 <= response.status_code < 300:
            err = self.__handle_response_error(response)
            raise err

        if request_opts.get('stream', False):
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
