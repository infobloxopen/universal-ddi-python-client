# UpdateRpzRuleResponse

The response format to update the RpzRule object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**RpzRule**](RpzRule.md) |  | [optional] 

## Example

```python
from dns_data.models.update_rpz_rule_response import UpdateRpzRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRpzRuleResponse from a JSON string
update_rpz_rule_response_instance = UpdateRpzRuleResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRpzRuleResponse.to_json())

# convert the object into a dict
update_rpz_rule_response_dict = update_rpz_rule_response_instance.to_dict()
# create an instance of UpdateRpzRuleResponse from a dict
update_rpz_rule_response_from_dict = UpdateRpzRuleResponse.from_dict(update_rpz_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


