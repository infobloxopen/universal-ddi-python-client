# PolicyTopologyRuleBinding

A __RuleBinding__ maps one __TopologyRulePreset__ (by _name_) to the destination to use when that preset matches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Optional. DNS code to return if the referenced preset matches. Must be set if _destination_ is _code_.  Allowed values: - nodata - nxdomain  Defaults to _nodata_. | [optional] 
**destination** | **str** | Destination of the matched __TopologyRulePreset__.  Allowed values: - code - pool  Defaults to _code_. | [optional] 
**name** | **str** | Required. Name of the __TopologyRulePreset__ from the referenced __Topology__. | 
**pool_id** | **str** | The resource identifier. | [optional] 

## Example

```python
from dtc.models.policy_topology_rule_binding import PolicyTopologyRuleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTopologyRuleBinding from a JSON string
policy_topology_rule_binding_instance = PolicyTopologyRuleBinding.from_json(json)
# print the JSON string representation of the object
print(PolicyTopologyRuleBinding.to_json())

# convert the object into a dict
policy_topology_rule_binding_dict = policy_topology_rule_binding_instance.to_dict()
# create an instance of PolicyTopologyRuleBinding from a dict
policy_topology_rule_binding_from_dict = PolicyTopologyRuleBinding.from_dict(policy_topology_rule_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


