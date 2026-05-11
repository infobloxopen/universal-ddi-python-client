# SNMPHealthCheckEntryCheck

Specific check for an SNMP entry and its value in MIB hierarchy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __EntryCheck__. | [optional] 
**max_value** | **str** | Optional. Expected max value of an entry to check against. Used for __in__ operator only, otherwise ignored. | [optional] 
**name** | **str** | Name is a dotted-decimal number that defines the location of the entry in the universal MIB tree. | 
**operator** | **str** | Operator defines operation to perform on an entry value.  Allowed values: * any - any value must be present * eq  - entry value must be equal to check&#39;s __value__. * leq - entry value must less or equal to check&#39;s __value__. * geq - entry value must be great or equal to check&#39;s __value__. * in  - entry value must be greater or equal than __value__ and less or equal than __max_value__.  Operator __in__ is supported only for __integer__ types. | 
**type** | **str** | Type defines type of an entry value.  Allowed values: * string * integer  String type does not support __in__ operator. | 
**value** | **str** | Optional. Expected value of an entry to check against. Ignored for __any__ operator. | [optional] 

## Example

```python
from dtc.models.snmp_health_check_entry_check import SNMPHealthCheckEntryCheck

# TODO update the JSON string below
json = "{}"
# create an instance of SNMPHealthCheckEntryCheck from a JSON string
snmp_health_check_entry_check_instance = SNMPHealthCheckEntryCheck.from_json(json)
# print the JSON string representation of the object
print(SNMPHealthCheckEntryCheck.to_json())

# convert the object into a dict
snmp_health_check_entry_check_dict = snmp_health_check_entry_check_instance.to_dict()
# create an instance of SNMPHealthCheckEntryCheck from a dict
snmp_health_check_entry_check_from_dict = SNMPHealthCheckEntryCheck.from_dict(snmp_health_check_entry_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


