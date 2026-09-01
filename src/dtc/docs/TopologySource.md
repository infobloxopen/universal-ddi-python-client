# TopologySource

A __TopologySource__ is a named source to be used in __TopologyRule__ objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. Display name of __TopologySource__. | 
**source** | **str** | Type of source.  Allowed values: - subnet - tag_rule  Required. | 
**subnets** | **List[str]** | Optional. List of subnets in CIDR format.  Must be set if _source_ is set to _subnet_, otherwise must be empty. | [optional] 
**tag_rules** | [**List[TagRule]**](TagRule.md) | Optional. List of tag rules to match against infrastructure source objects effective tags.  Must be set if _source_ is set to _tag_rule_, otherwise must be empty. | [optional] 

## Example

```python
from dtc.models.topology_source import TopologySource

# TODO update the JSON string below
json = "{}"
# create an instance of TopologySource from a JSON string
topology_source_instance = TopologySource.from_json(json)
# print the JSON string representation of the object
print(TopologySource.to_json())

# convert the object into a dict
topology_source_dict = topology_source_instance.to_dict()
# create an instance of TopologySource from a dict
topology_source_from_dict = TopologySource.from_dict(topology_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


