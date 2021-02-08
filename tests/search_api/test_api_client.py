from parameterized import parameterized
from unittest import mock
import unittest

from pydoof.search_api.api_client import SearchAPIClient
from pydoof.search_api import exceptions
import pydoof


def _exceptions_test_cases():
    return [
        (400, exceptions.BadRequestError),
        (403, exceptions.ForbiddenError),
        (404, exceptions.NotFoundError),
        (409, exceptions.InvalidTransformationError),
        (429, exceptions.QueryLimitReachedError),
        (500, exceptions.SearchAPIError)
    ]


def _name_func(func, _num, param):
    exception_name = parameterized.to_safe_name(param.args[1].__name__)
    return f'{func.__name__}_{exception_name.lower()}'


def _docstring_func(_func, _num, param):
    status, exc = param.args
    doc = f"Raise {exc.__name__} with {status} response"
    return doc


class TestAPIClient(unittest.TestCase):
    def tearDown(self):
        pydoof.search_url = None

    @parameterized.expand(_exceptions_test_cases,
                          name_func=_name_func,
                          doc_func=_docstring_func)
    @mock.patch('pydoof.base.requests')
    def test_raise(self, status_code, expected_exception,
                   requests_mock):
        response_mock = mock.Mock()
        response_mock.status_code = status_code
        response_mock.json.return_value = {
            'error': "Error message"
        }
        session_mock = mock.Mock()
        session_mock.request.return_value = response_mock
        requests_mock.Session.return_value = session_mock

        api_client = SearchAPIClient()
        with self.assertRaises(expected_exception) as cm:
            api_client.request('GET', url='/')

        self.assertEqual(cm.exception.message, 'Error message')

    @mock.patch('pydoof.base.requests')
    def test_can_set_global_host(self, requests_mock):
        response_mock = mock.Mock()
        response_mock.status_code = 200
        response_mock.text = 'OK'
        session_mock = mock.Mock()
        session_mock.request.return_value = response_mock
        requests_mock.Session.return_value = session_mock

        pydoof.search_url = 'https://eu1-search.doofinder.com'
        api_client = SearchAPIClient()
        api_client.request('GET', url='/')

        session_mock.request.assert_called_with(
            'GET', url='https://eu1-search.doofinder.com/',
            params=mock.ANY, json=mock.ANY, headers=mock.ANY, auth=mock.ANY
        )

    @mock.patch('pydoof.base.requests')
    def test_can_set_per_request_host(self, requests_mock):
        response_mock = mock.Mock()
        response_mock.status_code = 200
        response_mock.text = 'OK'
        session_mock = mock.Mock()
        session_mock.request.return_value = response_mock
        requests_mock.Session.return_value = session_mock

        pydoof.search_url = 'https://eu1-search.doofinder.com'
        api_client = SearchAPIClient(
            search_url='http://localhost:8000'
        )
        api_client.request('GET', url='/')

        session_mock.request.assert_called_with(
            'GET', url='http://localhost:8000/',
            params=mock.ANY, json=mock.ANY, headers=mock.ANY, auth=mock.ANY
        )
