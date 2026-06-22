# CreatePDPHealthCheckResponse

The __PDPHealthCheck__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**PDPHealthCheck**](PDPHealthCheck.md) | The created __PDPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.create_pdp_health_check_response import CreatePDPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePDPHealthCheckResponse from a JSON string
create_pdp_health_check_response_instance = CreatePDPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePDPHealthCheckResponse.to_json())

# convert the object into a dict
create_pdp_health_check_response_dict = create_pdp_health_check_response_instance.to_dict()
# create an instance of CreatePDPHealthCheckResponse from a dict
create_pdp_health_check_response_from_dict = CreatePDPHealthCheckResponse.from_dict(create_pdp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


