# ReadICMPHealthCheckResponse

The __ICMPHealthCheck__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ICMPHealthCheck**](ICMPHealthCheck.md) | The __ICMPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.read_icmp_health_check_response import ReadICMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadICMPHealthCheckResponse from a JSON string
read_icmp_health_check_response_instance = ReadICMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ReadICMPHealthCheckResponse.to_json())

# convert the object into a dict
read_icmp_health_check_response_dict = read_icmp_health_check_response_instance.to_dict()
# create an instance of ReadICMPHealthCheckResponse from a dict
read_icmp_health_check_response_from_dict = ReadICMPHealthCheckResponse.from_dict(read_icmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


