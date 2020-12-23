try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json.decoder import JSONDecodeError

from pydoof.base import APIClient
from pydoof.search_api import exceptions
import pydoof


class SearchAPIClient(APIClient):
    """
    Search API Client.

    This is the base client for Doofinder Search API. To use it, you must
    instance it with the `token` and `search_url` parameters. Or set those
    parameters in PyDoof.

        api_client = SearchAPIClient(
            search_url='https://eu1-search.doofinder.com',
            token='b8bcb...'
        )
        response = api_client.get('/5/search')
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = kwargs.get('search_url') or pydoof.search_url

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
