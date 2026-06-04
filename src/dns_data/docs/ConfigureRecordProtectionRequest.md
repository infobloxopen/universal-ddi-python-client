# ConfigureRecordProtectionRequest

The request format to configure record protection for multiple records in a zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_records** | [**List[ProtectedRecordItem]**](ProtectedRecordItem.md) | List of records with their protection levels. | [optional] 
**zone_id** | **str** | The resource identifier. | [optional] 

## Example

```python
from dns_data.models.configure_record_protection_request import ConfigureRecordProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureRecordProtectionRequest from a JSON string
configure_record_protection_request_instance = ConfigureRecordProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigureRecordProtectionRequest.to_json())

# convert the object into a dict
configure_record_protection_request_dict = configure_record_protection_request_instance.to_dict()
# create an instance of ConfigureRecordProtectionRequest from a dict
configure_record_protection_request_from_dict = ConfigureRecordProtectionRequest.from_dict(configure_record_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


