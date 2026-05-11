# UpdateICMPHealthCheckResponse

The __ICMPHealthCheck__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ICMPHealthCheck**](ICMPHealthCheck.md) | The __ICMPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.update_icmp_health_check_response import UpdateICMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateICMPHealthCheckResponse from a JSON string
update_icmp_health_check_response_instance = UpdateICMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateICMPHealthCheckResponse.to_json())

# convert the object into a dict
update_icmp_health_check_response_dict = update_icmp_health_check_response_instance.to_dict()
# create an instance of UpdateICMPHealthCheckResponse from a dict
update_icmp_health_check_response_from_dict = UpdateICMPHealthCheckResponse.from_dict(update_icmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


