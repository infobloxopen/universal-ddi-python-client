# ListHTTPHealthCheckResponse

The __HTTPHealthCheck__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HTTPHealthCheck]**](HTTPHealthCheck.md) | List of __HTTPHealthCheck__ objects. | [optional] 

## Example

```python
from dtc.models.list_http_health_check_response import ListHTTPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListHTTPHealthCheckResponse from a JSON string
list_http_health_check_response_instance = ListHTTPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ListHTTPHealthCheckResponse.to_json())

# convert the object into a dict
list_http_health_check_response_dict = list_http_health_check_response_instance.to_dict()
# create an instance of ListHTTPHealthCheckResponse from a dict
list_http_health_check_response_from_dict = ListHTTPHealthCheckResponse.from_dict(list_http_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


