# CreateTopologyResponse

The __Topology__ object create response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Topology**](Topology.md) | The created __Topology__ object. | [optional] 

## Example

```python
from dtc.models.create_topology_response import CreateTopologyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopologyResponse from a JSON string
create_topology_response_instance = CreateTopologyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTopologyResponse.to_json())

# convert the object into a dict
create_topology_response_dict = create_topology_response_instance.to_dict()
# create an instance of CreateTopologyResponse from a dict
create_topology_response_from_dict = CreateTopologyResponse.from_dict(create_topology_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


