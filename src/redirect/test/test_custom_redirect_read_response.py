# coding: utf-8

"""
    BloxOne Redirect API

    You can configure BloxOne Threat Defense Cloud to redirect traffic to the Infoblox server that displays the default or customized redirect page. You can redirect traffic to a custom destination using custom redirects. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from redirect.models.custom_redirect_read_response import CustomRedirectReadResponse


class TestCustomRedirectReadResponse(unittest.TestCase):
    """CustomRedirectReadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomRedirectReadResponse:
        """Test CustomRedirectReadResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomRedirectReadResponse`
        """
        model = CustomRedirectReadResponse()
        if include_optional:
            return CustomRedirectReadResponse(
                results = redirect.models.redirect_custom_redirect.redirectCustomRedirect(
                    created_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    data = '193.56.2.11, 193.56.2.12, 2001:db8:ffff:ffff:ffff:ffff:ffff:fff1', 
                    id = 56, 
                    name = 'custom_redirect_a', 
                    policy_ids = [245613, 12476], 
                    policy_names = [security_policy_a, security_policy_b], 
                    updated_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return CustomRedirectReadResponse(
        )
        """

    def testCustomRedirectReadResponse(self):
        """Test CustomRedirectReadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
