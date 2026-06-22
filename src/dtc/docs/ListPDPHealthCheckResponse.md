# ListPDPHealthCheckResponse

The __PDPHealthCheck__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PDPHealthCheck]**](PDPHealthCheck.md) | List of __PDPHealthCheck__ objects. | [optional] 

## Example

```python
from dtc.models.list_pdp_health_check_response import ListPDPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPDPHealthCheckResponse from a JSON string
list_pdp_health_check_response_instance = ListPDPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ListPDPHealthCheckResponse.to_json())

# convert the object into a dict
list_pdp_health_check_response_dict = list_pdp_health_check_response_instance.to_dict()
# create an instance of ListPDPHealthCheckResponse from a dict
list_pdp_health_check_response_from_dict = ListPDPHealthCheckResponse.from_dict(list_pdp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


