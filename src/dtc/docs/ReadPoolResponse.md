# ReadPoolResponse

The __Pool__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Pool**](Pool.md) | The __Pool__ object. | [optional] 

## Example

```python
from dtc.models.read_pool_response import ReadPoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadPoolResponse from a JSON string
read_pool_response_instance = ReadPoolResponse.from_json(json)
# print the JSON string representation of the object
print(ReadPoolResponse.to_json())

# convert the object into a dict
read_pool_response_dict = read_pool_response_instance.to_dict()
# create an instance of ReadPoolResponse from a dict
read_pool_response_from_dict = ReadPoolResponse.from_dict(read_pool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


