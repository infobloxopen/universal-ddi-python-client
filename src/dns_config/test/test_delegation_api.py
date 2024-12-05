# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.api.delegation_api import DelegationApi

from bloxone_client.api_client import ApiClient


class TestDelegationApi(unittest.TestCase):
    """DelegationApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = DelegationApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the Delegation object.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Moves the Delegation object to Recyclebin.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List Delegation objects.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Read the Delegation object.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the Delegation object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
