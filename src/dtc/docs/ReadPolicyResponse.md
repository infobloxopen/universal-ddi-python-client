# ReadPolicyResponse

The __Policy__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Policy**](Policy.md) | The __Policy__ object. | [optional] 

## Example

```python
from dtc.models.read_policy_response import ReadPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadPolicyResponse from a JSON string
read_policy_response_instance = ReadPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ReadPolicyResponse.to_json())

# convert the object into a dict
read_policy_response_dict = read_policy_response_instance.to_dict()
# create an instance of ReadPolicyResponse from a dict
read_policy_response_from_dict = ReadPolicyResponse.from_dict(read_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


