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

import pydoof2
from pydoof2.api.items_api import ItemsApi  # noqa: E501
from pydoof2.rest import ApiException


class TestItemsApi(unittest.TestCase):
    """ItemsApi unit test stubs"""

    def setUp(self):
        self.api = pydoof2.api.items_api.ItemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_item_create(self):
        """Test case for item_create

        Creates an item.  # noqa: E501
        """
        pass

    def test_item_delete(self):
        """Test case for item_delete

        Deletes an item.  # noqa: E501
        """
        pass

    def test_item_index(self):
        """Test case for item_index

        Scrolls through all items  # noqa: E501
        """
        pass

    def test_item_show(self):
        """Test case for item_show

        Get an item  # noqa: E501
        """
        pass

    def test_item_temp_create(self):
        """Test case for item_temp_create

        Creates an item in the temporal datatype  # noqa: E501
        """
        pass

    def test_item_temp_delete(self):
        """Test case for item_temp_delete

        Deletes an item in the temporal datatype  # noqa: E501
        """
        pass

    def test_item_temp_index(self):
        """Test case for item_temp_index

        Scrolls through all items from the temporal datatype  # noqa: E501
        """
        pass

    def test_item_temp_show(self):
        """Test case for item_temp_show

        Get an item from the temporal datatype  # noqa: E501
        """
        pass

    def test_item_temp_update(self):
        """Test case for item_temp_update

        Partially updates an item in the temporal datatype  # noqa: E501
        """
        pass

    def test_item_update(self):
        """Test case for item_update

        Partially updates an item.  # noqa: E501
        """
        pass

    def test_items_bulk_create(self):
        """Test case for items_bulk_create

        Creates items in bulk  # noqa: E501
        """
        pass

    def test_items_bulk_delete(self):
        """Test case for items_bulk_delete

        Deletes items in bulk  # noqa: E501
        """
        pass

    def test_items_bulk_update(self):
        """Test case for items_bulk_update

        Partial updates items in bulk  # noqa: E501
        """
        pass

    def test_items_temp_bulk_create(self):
        """Test case for items_temp_bulk_create

        Creates items in bulk in the temporal datatype  # noqa: E501
        """
        pass

    def test_items_temp_bulk_delete(self):
        """Test case for items_temp_bulk_delete

        Deletes items in bulk in the temporal datatype  # noqa: E501
        """
        pass

    def test_items_temp_bulk_update(self):
        """Test case for items_temp_bulk_update

        Partial updates items in bulk in the temporal datatype  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
