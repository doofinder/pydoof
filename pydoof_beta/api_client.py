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
            raise exceptions.APIConnectionError(
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

    def __handle_response_error(self, response):
        error_code = None
        http_status = response.status_code
        error_data = {'http_status': http_status}

        try:
            response_json = response.json()
            error = response_json['error']
            error_code = error['code']
        except (TypeError, KeyError, JSONDecodeError):
            error_data.update(http_body=response.text)
        else:
            error_data.update(**error)
        return self.__specific_error(http_status, error_code, error_data)

    def __specific_error(self, http_status, error_code, error_data):
        if http_status == 400:
            if error_code == 'bad_params':
                return exceptions.BadParametersError(**error_data)
            if error_code == 'index_internal_error':
                return exceptions.IndexInternalError(**error_data)
            if error_code == 'invalid_boost_value':
                return exceptions.InvalidBoostValueError(**error_data)
            if error_code == 'invalid_field_name':
                return exceptions.InvalidFieldNamesError(**error_data)
            else:
                return exceptions.BadRequestError(**error_data)
        elif http_status == 401:
            return exceptions.NotAuthenticatedError(**error_data)
        elif http_status == 403:
            return exceptions.AccessDeniedError(**error_data)
        elif http_status == 404:
            return exceptions.NotFoundError(**error_data)
        elif http_status == 408:
            return exceptions.APITimeoutError(**error_data)
        elif http_status == 409:
            if error_code == 'searchengine_locked':
                return exceptions.SearchEngineLockedError(**error_data)
            elif error_code == 'too_many_temporary':
                return exceptions.TooManyTemporaryError(**error_data)
            else:
                return exceptions.ConflictError(**error_data)
        elif http_status == 413:
            return exceptions.TooManyItemsError(**error_data)
        elif http_status == 429:
            return exceptions.TooManyRequestsError(**error_data)
        elif http_status == 502:
            error_data = {
                **error_data,
                'message': "Unexpected error communicating with Doofinder. "
                           "If this problem persists, let us know at "
                           "support@doofinder.com."
            }
            return exceptions.BadGatewayError(**error_data)
        else:
            return exceptions.PyDoofError(**error_data)


class ManagementApiClient(ApiClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        host = kwargs.get('management_host') or pydoof_beta.management_host
        if host is None:
            zone = kwargs.get('zone') or pydoof_beta.zone
            host = f'https://{zone}-api.doofinder.com'

        self.host = host


class SearchApiClient(ApiClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        host = kwargs.get('search_host') or pydoof_beta.search_host
        if host is None:
            zone = kwargs.get('zone') or pydoof_beta.zone
            host = f'https://{zone}-search.doofinder.com'

        self.host = host
