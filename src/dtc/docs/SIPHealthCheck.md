# SIPHealthCheck

A __SIPHealthCheck__ (_dtc/health_check_sip_) represents a DTC __Server__ health check that probes a Session Initiation Protocol (SIP) endpoint by sending a SIP OPTIONS request over TCP or UDP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __SIPHealthCheck__. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __SIPHealthCheck__. Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interval** | **int** | Optional. Interval value in seconds. The health check runs only for the specified interval and it is measured from the beginning of the previous check cycle. Defaults to _15_. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __SIPHealthCheck__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**name** | **str** | Display name of __SIPHealthCheck__. | 
**port** | **int** | Optional. Destination port for the SIP OPTIONS request. Defaults to _5060_ for both TCP and UDP transport. | [optional] 
**result_code** | **int** | Optional. Expected SIP response code, used with _CODE_IS_ and _CODE_IS_NOT_ result modes. Defaults to _200_. | [optional] 
**result_mode** | **str** | Optional. Defines how the SIP response code is evaluated. Supported values: _ANY_, _CODE_IS_, _CODE_IS_NOT_. Defaults to _CODE_IS_. | [optional] 
**retry_down** | **int** | Optional. Retry down count. The value determines how many bad health checks in a row must be received by the onprem host from the DTC Server for treating the health check as failed. Defaults to _1_. | [optional] 
**retry_up** | **int** | Optional. Retry up count. The value determines how many good health checks in a row must be received by the onprem host from the DTC Server for treating the health check as successful. Defaults to _1_. | [optional] 
**tags** | **object** | Optional. The tags for __SIPHealthCheck__ in JSON format. | [optional] 
**timeout** | **int** | Optional. Timeout value in seconds. The health check waits for the specified number of seconds after sending a request. If it does not receive a response within the number of seconds, then the health check is considered as failed. Defaults to _10_. | [optional] 
**transport** | **str** | Optional. Transport protocol for the SIP OPTIONS request. Supported values: _TCP_, _UDP_. Defaults to _TCP_. | [optional] 

## Example

```python
from dtc.models.sip_health_check import SIPHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of SIPHealthCheck from a JSON string
sip_health_check_instance = SIPHealthCheck.from_json(json)
# print the JSON string representation of the object
print(SIPHealthCheck.to_json())

# convert the object into a dict
sip_health_check_dict = sip_health_check_instance.to_dict()
# create an instance of SIPHealthCheck from a dict
sip_health_check_from_dict = SIPHealthCheck.from_dict(sip_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


