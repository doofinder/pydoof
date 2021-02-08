from parameterized import parameterized
from unittest import mock
import unittest

from pydoof.management_api.api_client import ManagementAPIClient
from pydoof.management_api import exceptions
import pydoof


def _exceptions_test_cases():
    return [
        (400, 'bad_params', exceptions.BadParametersError),
        (400, 'index_internal_error', exceptions.IndexInternalError),
        (400, 'invalid_boost_value', exceptions.InvalidBoostValueError),
        (400, 'invalid_field_name', exceptions.InvalidFieldNamesError),
        (400, '', exceptions.BadRequestError),
        (401, '', exceptions.NotAuthenticatedError),
        (403, '', exceptions.AccessDeniedError),
        (404, '', exceptions.NotFoundError),
        (408, '', exceptions.APITimeoutError),
        (409, 'searchengine_locked', exceptions.SearchEngineLockedError),
        (409, 'too_many_temporary', exceptions.TooManyTemporaryError),
        (409, '', exceptions.ConflictError),
        (413, '', exceptions.TooManyItemsError),
        (429, '', exceptions.TooManyRequestsError),
        (500, '', exceptions.ManagementAPIError),
        (502, '', exceptions.BadGatewayError)
    ]


def _name_func(func, _num, param):
    exception_name = parameterized.to_safe_name(param.args[2].__name__)
    return f'{func.__name__}_{exception_name.lower()}'


def _docstring_func(_func, _num, param):
    status, code, exc = param.args
    doc = f"Raise {exc.__name__} with {status} response"
    if code:
        doc += " and code {code}"
    return doc


class TestAPIClient(unittest.TestCase):
    def tearDown(self):
        pydoof.management_url = None

    @parameterized.expand(_exceptions_test_cases,
                          name_func=_name_func,
                          doc_func=_docstring_func)
    @mock.patch('pydoof.base.requests')
    def test_raise(self, status_code, error_code, expected_exception,
                   requests_mock):
        response_mock = mock.Mock()
        response_mock.status_code = status_code
        response_mock.json.return_value = {
            'error': {
                'code': error_code,
                'details': 'Details',
                'message': 'Message'
            }
        }
        session_mock = mock.Mock()
        session_mock.request.return_value = response_mock
        requests_mock.Session.return_value = session_mock

        api_client = ManagementAPIClient()
        with self.assertRaises(expected_exception) as cm:
            api_client.request('GET', url='/')

        self.assertEqual(cm.exception.details, 'Details')
        self.assertEqual(cm.exception.message, 'Message')

    @mock.patch('pydoof.base.requests')
    def test_can_set_global_host(self, requests_mock):
        response_mock = mock.Mock()
        response_mock.status_code = 200
        response_mock.text = 'OK'
        session_mock = mock.Mock()
        session_mock.request.return_value = response_mock
        requests_mock.Session.return_value = session_mock

        pydoof.management_url = 'https://eu1-api.doofinder.com'
        api_client = ManagementAPIClient()
        api_client.request('GET', url='/')

        session_mock.request.assert_called_with(
            'GET', url='https://eu1-api.doofinder.com/',
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

        pydoof.management_url = 'https://eu1-api.doofinder.com'
        api_client = ManagementAPIClient(
            management_url='http://localhost:8000'
        )
        api_client.request('GET', url='/')

        session_mock.request.assert_called_with(
            'GET', url='http://localhost:8000/',
            params=mock.ANY, json=mock.ANY, headers=mock.ANY, auth=mock.ANY
        )
