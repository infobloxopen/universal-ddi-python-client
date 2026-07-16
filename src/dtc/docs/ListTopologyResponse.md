# ListTopologyResponse

The __Topology__ object list response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Topology]**](Topology.md) | List of __Topology__ objects. | [optional] 

## Example

```python
from dtc.models.list_topology_response import ListTopologyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTopologyResponse from a JSON string
list_topology_response_instance = ListTopologyResponse.from_json(json)
# print the JSON string representation of the object
print(ListTopologyResponse.to_json())

# convert the object into a dict
list_topology_response_dict = list_topology_response_instance.to_dict()
# create an instance of ListTopologyResponse from a dict
list_topology_response_from_dict = ListTopologyResponse.from_dict(list_topology_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


