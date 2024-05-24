# coding: utf-8

"""
    Schedule Software/Config Updates

    Infoblox by default does automatic software updates when they become available. Updates are applied to all on-prem hosts, physical or virtual. However, you can override and schedule the software updates. You can also defer the updates to a later date and time. You can configure up to a total of 50 deferrals (scheduled and deferred software updates), which means you have the flexibility to create up to 50 update groups across different on-prem hosts by mapping with appropriate tags. Tags are be used to associate deferrals (scheduled or deferred) with a specific or group of onprem-hosts. Apart from software update deferrals, config update deferrals also can be configured using these overrides.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from upgrade_policy.models.deferred_window import DeferredWindow


class TestDeferredWindow(unittest.TestCase):
    """DeferredWindow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeferredWindow:
        """Test DeferredWindow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeferredWindow`
        """
        model = DeferredWindow()
        if include_optional:
            return DeferredWindow(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                enabled = True,
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DeferredWindow(
        )
        """

    def testDeferredWindow(self):
        """Test DeferredWindow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
