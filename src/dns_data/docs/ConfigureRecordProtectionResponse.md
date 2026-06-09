# ConfigureRecordProtectionResponse

The response format for configuring record protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_records** | [**List[ProtectedRecordItem]**](ProtectedRecordItem.md) | List of records with their protection levels and protection status. | [optional] 
**zone_id** | **str** | The resource identifier. | [optional] 

## Example

```python
from dns_data.models.configure_record_protection_response import ConfigureRecordProtectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureRecordProtectionResponse from a JSON string
configure_record_protection_response_instance = ConfigureRecordProtectionResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigureRecordProtectionResponse.to_json())

# convert the object into a dict
configure_record_protection_response_dict = configure_record_protection_response_instance.to_dict()
# create an instance of ConfigureRecordProtectionResponse from a dict
configure_record_protection_response_from_dict = ConfigureRecordProtectionResponse.from_dict(configure_record_protection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


