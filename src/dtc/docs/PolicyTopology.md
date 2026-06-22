# PolicyTopology

A __PolicyTopology__ binds a __Topology__ to a __Policy__ by mapping each __TopologyRulePreset__ (by _name_) to the destination (DNS code or __Pool__) to use when that preset matches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[PolicyTopologyRuleBinding]**](PolicyTopologyRuleBinding.md) | Ordered list of destination bindings, one per __TopologyRulePreset__ in the referenced __Topology__. Each binding maps a preset _name_ to the destination to use when that preset matches. | [optional] 
**topology_id** | **str** | The resource identifier. | 

## Example

```python
from dtc.models.policy_topology import PolicyTopology

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTopology from a JSON string
policy_topology_instance = PolicyTopology.from_json(json)
# print the JSON string representation of the object
print(PolicyTopology.to_json())

# convert the object into a dict
policy_topology_dict = policy_topology_instance.to_dict()
# create an instance of PolicyTopology from a dict
policy_topology_from_dict = PolicyTopology.from_dict(policy_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


