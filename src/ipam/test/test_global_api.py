# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam.api.global_api import GlobalApi

from universal_ddi_client.api_client import ApiClient


class TestGlobalApi(unittest.TestCase):
    """GlobalApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = GlobalApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_read(self) -> None:
        """Test case for read

        Retrieve the global configuration.
        """
        pass

    def test_read_by_id(self) -> None:
        """Test case for read_by_id

        Retrieve the global configuration.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the global configuration.
        """
        pass

    def test_update_by_id(self) -> None:
        """Test case for update_by_id

        Update the global configuration.
        """
        pass


if __name__ == '__main__':
    unittest.main()
