# SNMPUserSecurityModel

Parameters for user-based security model of SNMPv3.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_passphrase** | **str** | User passphrase for authentication. Ignored for __NoAuth__, otherwise mandatory. | [optional] 
**auth_protocol** | **str** | Authentication protocol.  Allowed values: * NoAuth * MD5 * SHA  Defaults to __NoAuth__. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**privacy_passphrase** | **str** | User passphrase for privacy. Ignored for __NoPrivacy__, otherwise mandatory. | [optional] 
**privacy_protocol** | **str** | Privacy protocol. Must be __NoPrivacy__ if auth_protocol set to __NoAuth__.  Allowed values: * NoPrivacy * DES * AES  Defaults to __NoPrivacy__. | [optional] 
**username** | **str** | User name with which to associate security information. | [optional] 

## Example

```python
from dtc.models.snmp_user_security_model import SNMPUserSecurityModel

# TODO update the JSON string below
json = "{}"
# create an instance of SNMPUserSecurityModel from a JSON string
snmp_user_security_model_instance = SNMPUserSecurityModel.from_json(json)
# print the JSON string representation of the object
print(SNMPUserSecurityModel.to_json())

# convert the object into a dict
snmp_user_security_model_dict = snmp_user_security_model_instance.to_dict()
# create an instance of SNMPUserSecurityModel from a dict
snmp_user_security_model_from_dict = SNMPUserSecurityModel.from_dict(snmp_user_security_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


