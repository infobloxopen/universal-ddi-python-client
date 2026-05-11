# ReadTCPHealthCheckResponse

The __TCPHealthCheck__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TCPHealthCheck**](TCPHealthCheck.md) | The __TCPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.read_tcp_health_check_response import ReadTCPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTCPHealthCheckResponse from a JSON string
read_tcp_health_check_response_instance = ReadTCPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ReadTCPHealthCheckResponse.to_json())

# convert the object into a dict
read_tcp_health_check_response_dict = read_tcp_health_check_response_instance.to_dict()
# create an instance of ReadTCPHealthCheckResponse from a dict
read_tcp_health_check_response_from_dict = ReadTCPHealthCheckResponse.from_dict(read_tcp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


