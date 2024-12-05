# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from fw.api.app_approvals_api import AppApprovalsApi

from bloxone_client.api_client import ApiClient


class TestAppApprovalsApi(unittest.TestCase):
    """AppApprovalsApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = AppApprovalsApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_list_app_approvals(self) -> None:
        """Test case for list_app_approvals

        """
        pass

    def test_replace_app_approvals(self) -> None:
        """Test case for replace_app_approvals

        Update Application Approval.
        """
        pass

    def test_update_app_approvals(self) -> None:
        """Test case for update_app_approvals

        """
        pass


if __name__ == '__main__':
    unittest.main()
