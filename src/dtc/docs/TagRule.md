# TagRule

A __TagRule__ is a single match criterion used by a tags-based topology rule source. Each rule carries a _key_, _value_, and an optional match _op_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Required. Tag key to match against a source object&#39;s effective tags. | 
**op** | **str** | Optional. Match operator.  Supported values: - EQUALS: matches when the key exists and its value equals the configured value. - NOT_EQUALS: matches when the key exists and all values for that key differ   from the configured value. A missing key does not satisfy either operator.  Defaults to _EQUALS_. | [optional] 
**value** | **str** | Required. Tag value to match against a source object&#39;s effective tags. | 

## Example

```python
from dtc.models.tag_rule import TagRule

# TODO update the JSON string below
json = "{}"
# create an instance of TagRule from a JSON string
tag_rule_instance = TagRule.from_json(json)
# print the JSON string representation of the object
print(TagRule.to_json())

# convert the object into a dict
tag_rule_dict = tag_rule_instance.to_dict()
# create an instance of TagRule from a dict
tag_rule_from_dict = TagRule.from_dict(tag_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


