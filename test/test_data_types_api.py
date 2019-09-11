# coding: utf-8

"""
    Doofinder API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@doofinder.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pydoof
from pydoof.api.data_types_api import DataTypesApi  # noqa: E501
from pydoof.rest import ApiException


class TestDataTypesApi(unittest.TestCase):
    """DataTypesApi unit test stubs"""

    def setUp(self):
        self.api = pydoof.api.data_types_api.DataTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_datatype_create(self):
        """Test case for datatype_create

        Create a datatype  # noqa: E501
        """
        pass

    def test_datatype_delete(self):
        """Test case for datatype_delete

        Delete a datatype  # noqa: E501
        """
        pass

    def test_datatype_index(self):
        """Test case for datatype_index

        List datatypes  # noqa: E501
        """
        pass

    def test_datatype_show(self):
        """Test case for datatype_show

        Get a datatype  # noqa: E501
        """
        pass

    def test_datatype_update(self):
        """Test case for datatype_update

        Update a datatype  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
