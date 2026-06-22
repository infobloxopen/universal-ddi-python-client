# UpdateSIPHealthCheckResponse

The __SIPHealthCheck__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SIPHealthCheck**](SIPHealthCheck.md) | The __SIPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.update_sip_health_check_response import UpdateSIPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSIPHealthCheckResponse from a JSON string
update_sip_health_check_response_instance = UpdateSIPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateSIPHealthCheckResponse.to_json())

# convert the object into a dict
update_sip_health_check_response_dict = update_sip_health_check_response_instance.to_dict()
# create an instance of UpdateSIPHealthCheckResponse from a dict
update_sip_health_check_response_from_dict = UpdateSIPHealthCheckResponse.from_dict(update_sip_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


