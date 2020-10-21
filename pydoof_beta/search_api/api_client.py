try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

from pydoof_beta.base import APIClient
from pydoof_beta.search_api import exceptions
import pydoof_beta


class SearchAPIClient(APIClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        host = kwargs.get('search_host') or pydoof_beta.search_host
        if host is None:
            zone = kwargs.get('zone') or pydoof_beta.zone
            host = f'https://{zone}-search.doofinder.com'

        self.host = host

    def _handle_response_error(self, response):
        http_status = response.status_code
        error_data = {'http_status': http_status}

        try:
            response_json = response.json()
            error_data['message'] = response_json['error']
        except (TypeError, KeyError, JSONDecodeError):
            error_data.update(http_body=response.text)
        return self.__get_error(http_status, error_data)

    def __get_error(self, http_status, error_data):
        errors_map = {
            400: exceptions.BadRequestError,
            403: exceptions.ForbiddenError,
            404: exceptions.NotFoundError,
            409: exceptions.InvalidTransformationError,
            429: exceptions.QueryLimitReachedError,
        }
        error = errors_map.get(http_status, exceptions.SearchAPIError)
        return error(**error_data)
