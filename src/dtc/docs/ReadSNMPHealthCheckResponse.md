# ReadSNMPHealthCheckResponse

The __SNMPHealthCheck__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SNMPHealthCheck**](SNMPHealthCheck.md) | The __SNMPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.read_snmp_health_check_response import ReadSNMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadSNMPHealthCheckResponse from a JSON string
read_snmp_health_check_response_instance = ReadSNMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ReadSNMPHealthCheckResponse.to_json())

# convert the object into a dict
read_snmp_health_check_response_dict = read_snmp_health_check_response_instance.to_dict()
# create an instance of ReadSNMPHealthCheckResponse from a dict
read_snmp_health_check_response_from_dict = ReadSNMPHealthCheckResponse.from_dict(read_snmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


