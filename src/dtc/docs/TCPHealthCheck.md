# TCPHealthCheck

A __TCPHealthCheck__ (_dtc/health_check_tcp_) represents a DTC __Server__ health check based on the Transmission Control Protocol (TCP).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __TCPHealthCheck__. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __TCPHealthCheck__. Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interval** | **int** | Optional. Interval value in seconds. The health check runs only for the specified interval and it is measured from the beginning of the previous check cycle. Defaults to _15_. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __TCPHealthCheck__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**name** | **str** | Display name of __TCPHealthCheck__. | 
**port** | **int** | Destination TCP port of __TCPHealthCheck__. | 
**retry_down** | **int** | Optional. Retry down count. The value determines how many bad health checks in a row must be received by the onprem host from the DTC Server for treating the health check as failed. Defaults to _1_. | [optional] 
**retry_up** | **int** | Optional. Retry up count. The value determines how many good health checks in a row must be received by the onprem host from the DTC Server for treating the health check as successful. Defaults to _1_. | [optional] 
**tags** | **object** | Optional. The tags for __TCPHealthCheck__ in JSON format. | [optional] 
**timeout** | **int** | Optional. Timeout value in seconds. The health check waits for the specified number of seconds after sending a request. If it does not receive a response within the number of seconds, then the health check is considered as failed. Defaults to _10_. | [optional] 

## Example

```python
from dtc.models.tcp_health_check import TCPHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of TCPHealthCheck from a JSON string
tcp_health_check_instance = TCPHealthCheck.from_json(json)
# print the JSON string representation of the object
print(TCPHealthCheck.to_json())

# convert the object into a dict
tcp_health_check_dict = tcp_health_check_instance.to_dict()
# create an instance of TCPHealthCheck from a dict
tcp_health_check_from_dict = TCPHealthCheck.from_dict(tcp_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


