import requests
try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

from pydoof_beta import exceptions
import pydoof_beta


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
        host = kwargs.get('management_host') or pydoof_beta.management_host
        if host is None:
            zone = kwargs.get('zone') or pydoof_beta.zone
            host = f'https://{zone}-api.doofinder.com'

        self.host = host
        self.headers = {'User-Agent': 'doofinder-api-client/python'}
        self.dfmaster_token = (
            kwargs.get('_dfmaster_token') or pydoof_beta._dfmaster_token
        )
        self.token = kwargs.get('token') or pydoof_beta.token

    @property
    def authentication(self):
        return DoofinderAuth(token=self.token,
                             dfmaster_token=self.dfmaster_token)

    def request(self, method, url, query_params=None, json=None, stream=False):
        try:
            response = requests.request(
                method,
                url=f'{self.host}{url}',
                params=query_params,
                json=json,
                headers=self.headers,
                auth=self.authentication
            )
        except Exception as exc:
            raise exceptions.APIConnectionError(
                message="Unexpected error communicating with Doofinder.",
                original_exc=exc
            )

        try:
            response_body = response.json()
        except JSONDecodeError:
            response_body = response.text

        if not 200 <= response.status_code < 300:
            error_code = None
            kwargs = {'http_status': response.status_code}
            try:
                error = response_body['error']
                error_code = error['code']
            except (TypeError, KeyError):
                kwargs = {'http_body': response_body}
            else:
                kwargs.update(**error)
            self.__handle_response_error(
                response.status_code, error_code, kwargs
            )

        return response_body

    def get(self, url, query_params=None):
        return self.request('GET', url, query_params)

    def delete(self, url, query_params=None):
        return self.request('DELETE', url, query_params)

    def post(self, url, json=None, query_params=None):
        return self.request('POST', url, query_params, json)

    def patch(self, url, json=None, query_params=None):
        return self.request('PATCH', url, query_params, json)

    def __handle_response_error(self, http_status, error_code, kwargs):
        if http_status == 400:
            if error_code == 'bad_params':
                raise exceptions.BadParametersError(**kwargs)
            if error_code == 'index_internal_error':
                raise exceptions.IndexInternalError(**kwargs)
            if error_code == 'invalid_boost_value':
                raise exceptions.InvalidBoostValueError(**kwargs)
            if error_code == 'invalid_field_name':
                raise exceptions.InvalidFieldNamesError(**kwargs)
            else:
                raise exceptions.BadRequestError(**kwargs)
        elif http_status == 401:
            raise exceptions.NotAuthenticatedError(**kwargs)
        elif http_status == 403:
            raise exceptions.AccessDeniedError(**kwargs)
        elif http_status == 404:
            raise exceptions.NotFoundError(**kwargs)
        elif http_status == 408:
            raise exceptions.APITimeoutError(**kwargs)
        elif http_status == 409:
            if error_code == 'searchengine_locked':
                raise exceptions.SearchEngineLockedError(**kwargs)
            elif error_code == 'too_many_temporary':
                raise exceptions.TooManyTemporaryError(**kwargs)
            else:
                raise exceptions.ConflictError(**kwargs)
        elif http_status == 413:
            raise exceptions.TooManyItemsError(**kwargs)
        elif http_status == 429:
            raise exceptions.TooManyRequestsError(**kwargs)
        elif http_status == 502:
            kwargs.update(
                message="Unexpected error communicating with Doofinder. "
                        "If this problem persists, let us know at "
                        "support@doofinder.com."
            )
            raise exceptions.BadGatewayError(**kwargs)
        else:
            raise exceptions.PyDoofError(**kwargs)
