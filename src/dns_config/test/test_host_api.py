# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a Universal DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured Universal DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.api.host_api import HostApi

from universal_ddi_client.api_client import ApiClient


class TestHostApi(unittest.TestCase):
    """HostApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = HostApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_list(self) -> None:
        """Test case for list

        List DNS Host objects.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Read the DNS Host object.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the DNS Host object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
