# Protection

Protection configuration indicates the record is protected & contains the user group with protected access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 

## Example

```python
from dns_data.models.protection import Protection

# TODO update the JSON string below
json = "{}"
# create an instance of Protection from a JSON string
protection_instance = Protection.from_json(json)
# print the JSON string representation of the object
print(Protection.to_json())

# convert the object into a dict
protection_dict = protection_instance.to_dict()
# create an instance of Protection from a dict
protection_from_dict = Protection.from_dict(protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


