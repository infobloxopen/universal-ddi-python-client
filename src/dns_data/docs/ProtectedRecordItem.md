# ProtectedRecordItem

Represents a single record protection configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | The protection level (e.g., \&quot;Global Admin\&quot;, \&quot;DDI Admin\&quot;, \&quot;None\&quot;). | [optional] 
**rname** | **str** | The record name (relative to zone). | [optional] 
**rtype** | **str** | The record type. | [optional] 

## Example

```python
from dns_data.models.protected_record_item import ProtectedRecordItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedRecordItem from a JSON string
protected_record_item_instance = ProtectedRecordItem.from_json(json)
# print the JSON string representation of the object
print(ProtectedRecordItem.to_json())

# convert the object into a dict
protected_record_item_dict = protected_record_item_instance.to_dict()
# create an instance of ProtectedRecordItem from a dict
protected_record_item_from_dict = ProtectedRecordItem.from_dict(protected_record_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


