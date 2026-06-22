# ReadSIPHealthCheckResponse

The __SIPHealthCheck__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SIPHealthCheck**](SIPHealthCheck.md) | The __SIPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.read_sip_health_check_response import ReadSIPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadSIPHealthCheckResponse from a JSON string
read_sip_health_check_response_instance = ReadSIPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ReadSIPHealthCheckResponse.to_json())

# convert the object into a dict
read_sip_health_check_response_dict = read_sip_health_check_response_instance.to_dict()
# create an instance of ReadSIPHealthCheckResponse from a dict
read_sip_health_check_response_from_dict = ReadSIPHealthCheckResponse.from_dict(read_sip_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


