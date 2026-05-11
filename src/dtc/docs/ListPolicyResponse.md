# ListPolicyResponse

The __Policy__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Policy]**](Policy.md) | List of __Policy__ objects. | [optional] 

## Example

```python
from dtc.models.list_policy_response import ListPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPolicyResponse from a JSON string
list_policy_response_instance = ListPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ListPolicyResponse.to_json())

# convert the object into a dict
list_policy_response_dict = list_policy_response_instance.to_dict()
# create an instance of ListPolicyResponse from a dict
list_policy_response_from_dict = ListPolicyResponse.from_dict(list_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


