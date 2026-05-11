# CreateSNMPHealthCheckResponse

The __SNMPHealthCheck__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SNMPHealthCheck**](SNMPHealthCheck.md) | The created __SNMPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.create_snmp_health_check_response import CreateSNMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSNMPHealthCheckResponse from a JSON string
create_snmp_health_check_response_instance = CreateSNMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSNMPHealthCheckResponse.to_json())

# convert the object into a dict
create_snmp_health_check_response_dict = create_snmp_health_check_response_instance.to_dict()
# create an instance of CreateSNMPHealthCheckResponse from a dict
create_snmp_health_check_response_from_dict = CreateSNMPHealthCheckResponse.from_dict(create_snmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


