# TopologyRule

A __TopologyRule__ represents a rule for topology load balancing method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Optional. DNS code to return if rule matches. Must be set if _destination_ is set to _code_.  Allowed values: - nodata - nxdomain  Defaults to _nodata_. | [optional] 
**destination** | **str** | Destination of __TopologyRule__.  Allowed values: - code - pool  Defaults to _code_. | [optional] 
**name** | **str** | Display name of __TopologyRule__. | 
**pool_id** | **str** | The resource identifier. | [optional] 
**source** | **str** | Type of source.  Allowed values: - subnet - tags - default  Defaults to _default_. | [optional] 
**subnets** | **List[str]** | Optional. List of subnets in CIDR format.  Must be set if _source_ is _subnet_, otherwise must be empty. | [optional] 
**tags** | [**List[TagRule]**](TagRule.md) | Optional. List of tag rules to match against a source object&#39;s effective tags. Effective tags &#x3D; direct tags plus tags inherited from the IPAM parent chain (IPSpace → Address Block → Subnet); the closer level wins on key conflicts. All rules use AND semantics: an object must satisfy every __TagRule__ to match.  Must be set if _source_ is _tags_, otherwise must be empty. | [optional] 

## Example

```python
from dtc.models.topology_rule import TopologyRule

# TODO update the JSON string below
json = "{}"
# create an instance of TopologyRule from a JSON string
topology_rule_instance = TopologyRule.from_json(json)
# print the JSON string representation of the object
print(TopologyRule.to_json())

# convert the object into a dict
topology_rule_dict = topology_rule_instance.to_dict()
# create an instance of TopologyRule from a dict
topology_rule_from_dict = TopologyRule.from_dict(topology_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


