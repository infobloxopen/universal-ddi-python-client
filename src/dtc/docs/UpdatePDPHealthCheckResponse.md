# UpdatePDPHealthCheckResponse

The __PDPHealthCheck__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**PDPHealthCheck**](PDPHealthCheck.md) | The __PDPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.update_pdp_health_check_response import UpdatePDPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePDPHealthCheckResponse from a JSON string
update_pdp_health_check_response_instance = UpdatePDPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePDPHealthCheckResponse.to_json())

# convert the object into a dict
update_pdp_health_check_response_dict = update_pdp_health_check_response_instance.to_dict()
# create an instance of UpdatePDPHealthCheckResponse from a dict
update_pdp_health_check_response_from_dict = UpdatePDPHealthCheckResponse.from_dict(update_pdp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


