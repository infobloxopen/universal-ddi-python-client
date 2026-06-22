# ReadTopologyResponse

The __Topology__ object read response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Topology**](Topology.md) | The __Topology__ object. | [optional] 

## Example

```python
from dtc.models.read_topology_response import ReadTopologyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTopologyResponse from a JSON string
read_topology_response_instance = ReadTopologyResponse.from_json(json)
# print the JSON string representation of the object
print(ReadTopologyResponse.to_json())

# convert the object into a dict
read_topology_response_dict = read_topology_response_instance.to_dict()
# create an instance of ReadTopologyResponse from a dict
read_topology_response_from_dict = ReadTopologyResponse.from_dict(read_topology_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


