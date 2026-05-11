# UpdatePolicyResponse

The __Policy__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Policy**](Policy.md) | The __Policy__ object. | [optional] 

## Example

```python
from dtc.models.update_policy_response import UpdatePolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePolicyResponse from a JSON string
update_policy_response_instance = UpdatePolicyResponse.from_json(json)
# print the JSON string representation of the object
print(UpdatePolicyResponse.to_json())

# convert the object into a dict
update_policy_response_dict = update_policy_response_instance.to_dict()
# create an instance of UpdatePolicyResponse from a dict
update_policy_response_from_dict = UpdatePolicyResponse.from_dict(update_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


