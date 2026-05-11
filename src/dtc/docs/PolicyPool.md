# PolicyPool

A __PolicyPool__ represents a link between __Policy__ and __Pool__.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of __Pool__. | [optional] [readonly] 
**pool_id** | **str** | The resource identifier. | 
**weight** | **int** | Weight of __Pool__ to be used for load balancing. Unsigned integer, min 1; max 65535. | 

## Example

```python
from dtc.models.policy_pool import PolicyPool

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyPool from a JSON string
policy_pool_instance = PolicyPool.from_json(json)
# print the JSON string representation of the object
print(PolicyPool.to_json())

# convert the object into a dict
policy_pool_dict = policy_pool_instance.to_dict()
# create an instance of PolicyPool from a dict
policy_pool_from_dict = PolicyPool.from_dict(policy_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


