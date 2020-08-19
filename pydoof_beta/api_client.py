from json import JSONDecodeError
import requests

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

    def request(self, method, url, query_params=None, json=None):
        response = requests.request(
            method,
            url=f'{self.host}{url}',
            params=query_params,
            json=json,
            headers=self.headers,
            auth=self.authentication
        )
        try:
            response_body = response.json()
        except JSONDecodeError:
            response_body = response.text

        if not 200 <= response.status_code < 300:
            self.__handle_error(response.status_code, response_body)

        return response_body

    def get(self, url, query_params=None):
        return self.request('GET', url, query_params)

    def delete(self, url, query_params=None):
        return self.request('DELETE', url, query_params)

    def post(self, url, json=None, query_params=None):
        return self.request('POST', url, query_params, json)

    def patch(self, url, json=None, query_params=None):
        return self.request('PATCH', url, query_params, json)

    def __handle_error(self, e_status, e_body):
        e_code = None
        try:
            error = e_body["error"]
            e_code = error["code"]
        except (TypeError, KeyError):
            kwargs = {'message': e_body}
        else:
            kwargs = {'error_body': error}

        e_klass = self.__get_error_class(e_status, e_code)
        raise e_klass(**kwargs)

    def __get_error_class(self, e_status, e_code):
        if e_status == 400:
            if e_code == 'bad_params':
                return exceptions.BadParametersError
            if e_code == 'index_internal_error':
                return exceptions.IndexInternalError
            if e_code == 'invalid_boost_value':
                return exceptions.InvalidBoostValueError
            if e_code == 'invalid_field_name':
                return exceptions.InvalidFieldNamesError
            else:
                return exceptions.BadRequestError
        elif e_status == 401:
            return exceptions.NotAuthenticatedError
        elif e_status == 403:
            return exceptions.AccessDeniedError
        elif e_status == 404:
            return exceptions.NotFoundError
        elif e_status == 408:
            return exceptions.APITimeoutError
        elif e_status == 409:
            if e_code == 'searchengine_locked':
                return exceptions.NotFoundError
            elif e_code == 'too_many_temporary':
                return exceptions.TooManyTemporaryError
            else:
                return exceptions.ConflictError
        elif e_status == 413:
            return exceptions.TooManyItemsError
        elif e_status == 429:
            return exceptions.TooManyRequestsError
        else:
            return exceptions.PyDoofError
