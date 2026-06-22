# TopologyRulePreset

A __TopologyRulePreset__ is a named set of match criteria for classifying infrastructure source objects. A __Topology__ holds an ordered list of __TopologyRulePreset__ objects evaluated top to bottom; the first preset whose criteria all match wins. Destination (DNS code or __Pool__) is configured separately per __Policy__ in __PolicyTopology.RuleBinding__, not on the preset itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. Display name of __TopologyRulePreset__. Must be unique within __Topology__. | 
**source** | **str** | Type of source.  Allowed values: - subnet - tags - default  Defaults to _default_. | [optional] 
**subnets** | **List[str]** | Optional. List of subnets in CIDR format.  Must be set if _source_ is _subnet_, otherwise must be empty. | [optional] 
**tags** | [**List[TagRule]**](TagRule.md) | Optional. List of tag rules to match against a source object&#39;s effective tags. Effective tags &#x3D; direct tags plus tags inherited from the IPAM parent chain (IPSpace → Address Block → Subnet); the closer level wins on key conflicts. All rules use AND semantics: an object must satisfy every __TagRule__ to match.  Must be set if _source_ is _tags_, otherwise must be empty. | [optional] 

## Example

```python
from dtc.models.topology_rule_preset import TopologyRulePreset

# TODO update the JSON string below
json = "{}"
# create an instance of TopologyRulePreset from a JSON string
topology_rule_preset_instance = TopologyRulePreset.from_json(json)
# print the JSON string representation of the object
print(TopologyRulePreset.to_json())

# convert the object into a dict
topology_rule_preset_dict = topology_rule_preset_instance.to_dict()
# create an instance of TopologyRulePreset from a dict
topology_rule_preset_from_dict = TopologyRulePreset.from_dict(topology_rule_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


