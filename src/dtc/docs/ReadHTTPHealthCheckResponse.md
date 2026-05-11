# ReadHTTPHealthCheckResponse

The __HTTPHealthCheck__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HTTPHealthCheck**](HTTPHealthCheck.md) | The __HTTPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.read_http_health_check_response import ReadHTTPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadHTTPHealthCheckResponse from a JSON string
read_http_health_check_response_instance = ReadHTTPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ReadHTTPHealthCheckResponse.to_json())

# convert the object into a dict
read_http_health_check_response_dict = read_http_health_check_response_instance.to_dict()
# create an instance of ReadHTTPHealthCheckResponse from a dict
read_http_health_check_response_from_dict = ReadHTTPHealthCheckResponse.from_dict(read_http_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


