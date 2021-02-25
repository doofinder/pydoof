from unittest import mock
import unittest

from pydoof.management_api import indices


class TestIndices(unittest.TestCase):
    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_list(self, APIClientMock):
        hashid = 'aab32d8'

        indices.list(hashid)

        APIClientMock.return_value.get.assert_called_with(
            f'/api/v2/search_engines/{hashid}/indices'
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_create(self, APIClientMock):
        hashid = 'aab32d8'
        data = {'data': 'DATA'}

        indices.create(hashid, data)

        APIClientMock.return_value.post.assert_called_with(
            f'/api/v2/search_engines/{hashid}/indices', data
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_get(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.get(hashid, index_name)

        APIClientMock.return_value.get.assert_called_with(
            f'/api/v2/search_engines/{hashid}/indices/{index_name}'
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_update(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'
        data = {'data': 'DATA'}

        indices.update(hashid, index_name, data)

        APIClientMock.return_value.patch.assert_called_with(
            f'/api/v2/search_engines/{hashid}/indices/{index_name}', data
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_delete(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.delete(hashid, index_name)

        APIClientMock.return_value.delete.assert_called_with(
            f'/api/v2/search_engines/{hashid}/indices/{index_name}'
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_create_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.create_temp(hashid, index_name)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp',
            query_params={}
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_delete_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.delete_temp(hashid, index_name)

        APIClientMock.return_value.delete.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/temp'
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_reindex_to_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.reindex_to_temp(hashid, index_name)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/_reindex_to_temp',
            query_params={}
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_get_reindex_status(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.get_reindex_status(hashid, index_name)

        APIClientMock.return_value.get.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/_reindex_to_temp'
        )

    @mock.patch('pydoof.management_api.indices.ManagementAPIClient')
    def test_replace_by_temp(self, APIClientMock):
        hashid = 'aab32d8'
        index_name = 'product'

        indices.replace_by_temp(hashid, index_name)

        APIClientMock.return_value.post.assert_called_with(
            '/api/v2/search_engines/aab32d8/indices/product/_replace_by_temp'
        )
