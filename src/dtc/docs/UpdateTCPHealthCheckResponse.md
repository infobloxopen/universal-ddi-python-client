# UpdateTCPHealthCheckResponse

The __TCPHealthCheck__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TCPHealthCheck**](TCPHealthCheck.md) | The __TCPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.update_tcp_health_check_response import UpdateTCPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTCPHealthCheckResponse from a JSON string
update_tcp_health_check_response_instance = UpdateTCPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTCPHealthCheckResponse.to_json())

# convert the object into a dict
update_tcp_health_check_response_dict = update_tcp_health_check_response_instance.to_dict()
# create an instance of UpdateTCPHealthCheckResponse from a dict
update_tcp_health_check_response_from_dict = UpdateTCPHealthCheckResponse.from_dict(update_tcp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


