try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

from pydoof_beta.base import APIClient
from pydoof_beta.management_api import exceptions
import pydoof_beta


class ManagementAPIClient(APIClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = kwargs.get('management_url') or pydoof_beta.management_url

    def _handle_response_error(self, response):
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
        return self.__get_error(http_status, error_code, error_data)

    def __get_error(self, http_status, error_code, error_data):
        errors_map = {
            400: self.__get_400_error(error_code),
            401: exceptions.NotAuthenticatedError,
            403: exceptions.AccessDeniedError,
            404: exceptions.NotFoundError,
            408: exceptions.APITimeoutError,
            409: self.__get_409_error(error_code),
            413: exceptions.TooManyItemsError,
            429: exceptions.TooManyRequestsError,
            502: exceptions.BadGatewayError,

        }
        error = errors_map.get(http_status, exceptions.ManagementAPIError)
        return error(**error_data)

    def __get_400_error(self, error_code):
        errors_map = {
            'bad_params': exceptions.BadParametersError,
            'index_internal_error': exceptions.IndexInternalError,
            'invalid_boost_value': exceptions.InvalidBoostValueError,
            'invalid_field_name': exceptions.InvalidFieldNamesError
        }
        return errors_map.get(error_code, exceptions.BadRequestError)

    def __get_409_error(self, error_code):
        errors_map = {
            'searchengine_locked': exceptions.SearchEngineLockedError,
            'too_many_temporary': exceptions.TooManyTemporaryError
        }
        return errors_map.get(error_code, exceptions.ConflictError)
