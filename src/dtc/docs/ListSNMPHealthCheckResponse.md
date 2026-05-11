# ListSNMPHealthCheckResponse

The __SNMPHealthCheck__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[SNMPHealthCheck]**](SNMPHealthCheck.md) | List of __SNMPHealthCheck__ objects. | [optional] 

## Example

```python
from dtc.models.list_snmp_health_check_response import ListSNMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSNMPHealthCheckResponse from a JSON string
list_snmp_health_check_response_instance = ListSNMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ListSNMPHealthCheckResponse.to_json())

# convert the object into a dict
list_snmp_health_check_response_dict = list_snmp_health_check_response_instance.to_dict()
# create an instance of ListSNMPHealthCheckResponse from a dict
list_snmp_health_check_response_from_dict = ListSNMPHealthCheckResponse.from_dict(list_snmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


