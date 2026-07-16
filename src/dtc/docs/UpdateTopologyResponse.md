# UpdateTopologyResponse

The __Topology__ object update response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Topology**](Topology.md) | The __Topology__ object. | [optional] 

## Example

```python
from dtc.models.update_topology_response import UpdateTopologyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTopologyResponse from a JSON string
update_topology_response_instance = UpdateTopologyResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTopologyResponse.to_json())

# convert the object into a dict
update_topology_response_dict = update_topology_response_instance.to_dict()
# create an instance of UpdateTopologyResponse from a dict
update_topology_response_from_dict = UpdateTopologyResponse.from_dict(update_topology_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


