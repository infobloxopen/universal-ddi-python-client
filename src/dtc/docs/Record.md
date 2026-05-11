# Record

__Record__ represents a resource record which is returned in response to load balanced DNS queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_rdata** | **str** | The DNS protocol textual representation of the record data. | [optional] [readonly] 
**rdata** | **object** | JSON representation of resource record data. | 
**type** | **str** | Resource record type.  List of supported types: * _A_ (_TYPE1_) * _AAAA_ (_TYPE28_) * _CNAME_ (_TYPE5_) * _HTTPS_ (_TYPE65_) * _SRV_ (_TYPE33_) * _SVCB_ (_TYPE64_) | 

## Example

```python
from dtc.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_from_dict = Record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


