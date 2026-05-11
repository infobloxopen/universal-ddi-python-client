# UpdatePoolResponse

The __Pool__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Pool**](Pool.md) | The __Pool__ object. | [optional] 

## Example

```python
from dtc.models.update_pool_response import UpdatePoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePoolResponse from a JSON string
update_pool_response_instance = UpdatePoolResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePoolResponse.to_json())

# convert the object into a dict
update_pool_response_dict = update_pool_response_instance.to_dict()
# create an instance of UpdatePoolResponse from a dict
update_pool_response_from_dict = UpdatePoolResponse.from_dict(update_pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


