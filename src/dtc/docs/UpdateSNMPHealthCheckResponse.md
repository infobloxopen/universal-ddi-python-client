# UpdateSNMPHealthCheckResponse

The __SNMPHealthCheck__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SNMPHealthCheck**](SNMPHealthCheck.md) | The __SNMPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.update_snmp_health_check_response import UpdateSNMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSNMPHealthCheckResponse from a JSON string
update_snmp_health_check_response_instance = UpdateSNMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSNMPHealthCheckResponse.to_json())

# convert the object into a dict
update_snmp_health_check_response_dict = update_snmp_health_check_response_instance.to_dict()
# create an instance of UpdateSNMPHealthCheckResponse from a dict
update_snmp_health_check_response_from_dict = UpdateSNMPHealthCheckResponse.from_dict(update_snmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


