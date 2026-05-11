# UpdateHTTPHealthCheckResponse

The __HTTPHealthCheck__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**HTTPHealthCheck**](HTTPHealthCheck.md) | The __HTTPHealthCheck__ object. | [optional] 

## Example

```python
from dtc.models.update_http_health_check_response import UpdateHTTPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHTTPHealthCheckResponse from a JSON string
update_http_health_check_response_instance = UpdateHTTPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateHTTPHealthCheckResponse.to_json())

# convert the object into a dict
update_http_health_check_response_dict = update_http_health_check_response_instance.to_dict()
# create an instance of UpdateHTTPHealthCheckResponse from a dict
update_http_health_check_response_from_dict = UpdateHTTPHealthCheckResponse.from_dict(update_http_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


