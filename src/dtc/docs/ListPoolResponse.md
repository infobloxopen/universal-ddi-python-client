# ListPoolResponse

The __Pool__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Pool]**](Pool.md) | List of __Pool__ objects. | [optional] 

## Example

```python
from dtc.models.list_pool_response import ListPoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPoolResponse from a JSON string
list_pool_response_instance = ListPoolResponse.from_json(json)
# print the JSON string representation of the object
print(ListPoolResponse.to_json())

# convert the object into a dict
list_pool_response_dict = list_pool_response_instance.to_dict()
# create an instance of ListPoolResponse from a dict
list_pool_response_from_dict = ListPoolResponse.from_dict(list_pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


