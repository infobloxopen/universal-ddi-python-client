# ReadPDPHealthCheckResponse

The __PDPHealthCheck__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**PDPHealthCheck**](PDPHealthCheck.md) | The __PDPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.read_pdp_health_check_response import ReadPDPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadPDPHealthCheckResponse from a JSON string
read_pdp_health_check_response_instance = ReadPDPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ReadPDPHealthCheckResponse.to_json())

# convert the object into a dict
read_pdp_health_check_response_dict = read_pdp_health_check_response_instance.to_dict()
# create an instance of ReadPDPHealthCheckResponse from a dict
read_pdp_health_check_response_from_dict = ReadPDPHealthCheckResponse.from_dict(read_pdp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


