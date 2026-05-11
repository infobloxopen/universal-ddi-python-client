# ListICMPHealthCheckResponse

The __ICMPHealthCheck__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ICMPHealthCheck]**](ICMPHealthCheck.md) | List of __ICMPHealthCheck__ objects. | [optional] 

## Example

```python
from dtc.models.list_icmp_health_check_response import ListICMPHealthCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListICMPHealthCheckResponse from a JSON string
list_icmp_health_check_response_instance = ListICMPHealthCheckResponse.from_json(json)
# print the JSON string representation of the object
print(ListICMPHealthCheckResponse.to_json())

# convert the object into a dict
list_icmp_health_check_response_dict = list_icmp_health_check_response_instance.to_dict()
# create an instance of ListICMPHealthCheckResponse from a dict
list_icmp_health_check_response_from_dict = ListICMPHealthCheckResponse.from_dict(list_icmp_health_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


