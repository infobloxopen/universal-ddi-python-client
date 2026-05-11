# CreateICMPHealthCheckResponse

The __ICMPHealthCheck__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ICMPHealthCheck**](ICMPHealthCheck.md) | The created __ICMPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.create_icmp_health_check_response import CreateICMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateICMPHealthCheckResponse from a JSON string
create_icmp_health_check_response_instance = CreateICMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(CreateICMPHealthCheckResponse.to_json())

# convert the object into a dict
create_icmp_health_check_response_dict = create_icmp_health_check_response_instance.to_dict()
# create an instance of CreateICMPHealthCheckResponse from a dict
create_icmp_health_check_response_from_dict = CreateICMPHealthCheckResponse.from_dict(create_icmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


