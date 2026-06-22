# CreateSIPHealthCheckResponse

The __SIPHealthCheck__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SIPHealthCheck**](SIPHealthCheck.md) | The created __SIPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.create_sip_health_check_response import CreateSIPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSIPHealthCheckResponse from a JSON string
create_sip_health_check_response_instance = CreateSIPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSIPHealthCheckResponse.to_json())

# convert the object into a dict
create_sip_health_check_response_dict = create_sip_health_check_response_instance.to_dict()
# create an instance of CreateSIPHealthCheckResponse from a dict
create_sip_health_check_response_from_dict = CreateSIPHealthCheckResponse.from_dict(create_sip_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


