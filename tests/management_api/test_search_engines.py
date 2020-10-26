from unittest import mock
import unittest

from pydoof.management_api import search_engines


class TestSearchEngines(unittest.TestCase):
    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_list(self, APIClientMock):
        search_engines.list()

        APIClientMock.return_value.get.assert_called_with(
            '/api/v2/search_engines'
        )

    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_create(self, APIClientMock):
        data = {'data': 'DATA'}

        search_engines.create(data)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines', data
        )

    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_get(self, APIClientMock):
        hashid = 'aab32d8'

        search_engines.get(hashid)

        APIClientMock.return_value.get.assert_called_with(
            f'/api/v2/search_engines/{hashid}'
        )

    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_update(self, APIClientMock):
        hashid = 'aab32d8'
        data = {'data': 'DATA'}

        search_engines.update(hashid, data)

        APIClientMock.return_value.patch.assert_called_with(
            f'/api/v2/search_engines/{hashid}', data
        )

    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_delete(self, APIClientMock):
        hashid = 'aab32d8'

        search_engines.delete(hashid)

        APIClientMock.return_value.delete.assert_called_with(
            f'/api/v2/search_engines/{hashid}'
        )

    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_schedule_process(self, APIClientMock):
        hashid = 'aab32d8'

        search_engines.schedule_process(hashid)

        APIClientMock.return_value.post.assert_called_with(
            f'/api/v2/search_engines/{hashid}/_process'
        )

    @mock.patch('pydoof.management_api.search_engines.ManagementAPIClient')
    def test_get_process_status(self, APIClientMock):
        hashid = 'aab32d8'

        search_engines.get_process_status(hashid)

        APIClientMock.return_value.get.assert_called_with(
            f'/api/v2/search_engines/{hashid}/_process'
        )
