# Topology

A __Topology__ (_dtc/topology_) is a reusable, named set of __TopologyRulePreset__ objects that provide deterministic infrastructure classification for DTC __Policy__ evaluation using infrastructure source object tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __Topology__. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __Topology__.  Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __Topology__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**name** | **str** | Display name of __Topology__. | 
**rules** | [**List[TopologyRulePreset]**](TopologyRulePreset.md) | List of __TopologyRulePreset__ objects defining the resolving strategy for __Policy__. Preset names must be unique within __Topology__.  Defaults to a list with a single, default __TopologyRulePreset__. | [optional] 
**tags** | **object** | Optional. The tags for __Topology__ in JSON format. | [optional] 

## Example

```python
from dtc.models.topology import Topology

# TODO update the JSON string below
json = "{}"
# create an instance of Topology from a JSON string
topology_instance = Topology.from_json(json)
# print the JSON string representation of the object
print(Topology.to_json())

# convert the object into a dict
topology_dict = topology_instance.to_dict()
# create an instance of Topology from a dict
topology_from_dict = Topology.from_dict(topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


