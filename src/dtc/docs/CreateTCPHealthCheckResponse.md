# CreateTCPHealthCheckResponse

The __TCPHealthCheck__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TCPHealthCheck**](TCPHealthCheck.md) | The created __TCPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.create_tcp_health_check_response import CreateTCPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTCPHealthCheckResponse from a JSON string
create_tcp_health_check_response_instance = CreateTCPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTCPHealthCheckResponse.to_json())

# convert the object into a dict
create_tcp_health_check_response_dict = create_tcp_health_check_response_instance.to_dict()
# create an instance of CreateTCPHealthCheckResponse from a dict
create_tcp_health_check_response_from_dict = CreateTCPHealthCheckResponse.from_dict(create_tcp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


