# PoolServer

A __PoolServer__ represents a link between __Pool__ and __Server__.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of __Server__. | [optional] [readonly] 
**server_id** | **str** | The resource identifier. | 
**weight** | **int** | Weight of __Server__ to be used for load balancing. Unsigned integer, min 1; max 65535. | 

## Example

```python
from dtc.models.pool_server import PoolServer

# TODO update the JSON string below
json = "{}"
# create an instance of PoolServer from a JSON string
pool_server_instance = PoolServer.from_json(json)
# print the JSON string representation of the object
print(PoolServer.to_json())

# convert the object into a dict
pool_server_dict = pool_server_instance.to_dict()
# create an instance of PoolServer from a dict
pool_server_from_dict = PoolServer.from_dict(pool_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


