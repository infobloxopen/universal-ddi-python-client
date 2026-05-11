# CreatePoolResponse

The __Pool__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Pool**](Pool.md) | The created __Pool__ object. | [optional] 

## Example

```python
from dtc.models.create_pool_response import CreatePoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePoolResponse from a JSON string
create_pool_response_instance = CreatePoolResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePoolResponse.to_json())

# convert the object into a dict
create_pool_response_dict = create_pool_response_instance.to_dict()
# create an instance of CreatePoolResponse from a dict
create_pool_response_from_dict = CreatePoolResponse.from_dict(create_pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


