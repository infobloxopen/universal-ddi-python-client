# CreateHTTPHealthCheckResponse

The __HTTPHealthCheck__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HTTPHealthCheck**](HTTPHealthCheck.md) | The created __HTTPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.create_http_health_check_response import CreateHTTPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHTTPHealthCheckResponse from a JSON string
create_http_health_check_response_instance = CreateHTTPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHTTPHealthCheckResponse.to_json())

# convert the object into a dict
create_http_health_check_response_dict = create_http_health_check_response_instance.to_dict()
# create an instance of CreateHTTPHealthCheckResponse from a dict
create_http_health_check_response_from_dict = CreateHTTPHealthCheckResponse.from_dict(create_http_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


