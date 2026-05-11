# CreatePolicyResponse

The __Policy__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Policy**](Policy.md) | The created __Policy__ object. | [optional] 

## Example

```python
from dtc.models.create_policy_response import CreatePolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePolicyResponse from a JSON string
create_policy_response_instance = CreatePolicyResponse.from_json(json)
# print the JSON string representation of the object
print(CreatePolicyResponse.to_json())

# convert the object into a dict
create_policy_response_dict = create_policy_response_instance.to_dict()
# create an instance of CreatePolicyResponse from a dict
create_policy_response_from_dict = CreatePolicyResponse.from_dict(create_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


