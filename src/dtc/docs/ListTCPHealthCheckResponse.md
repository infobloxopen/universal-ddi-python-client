# ListTCPHealthCheckResponse

The __TCPHealthCheck__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TCPHealthCheck]**](TCPHealthCheck.md) | List of __TCPHealthCheck__ objects. | [optional] 

## Example

```python
from dtc.models.list_tcp_health_check_response import ListTCPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTCPHealthCheckResponse from a JSON string
list_tcp_health_check_response_instance = ListTCPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ListTCPHealthCheckResponse.to_json())

# convert the object into a dict
list_tcp_health_check_response_dict = list_tcp_health_check_response_instance.to_dict()
# create an instance of ListTCPHealthCheckResponse from a dict
list_tcp_health_check_response_from_dict = ListTCPHealthCheckResponse.from_dict(list_tcp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


