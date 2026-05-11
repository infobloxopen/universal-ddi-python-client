# PoolHealthCheck

A __PoolHealthCheck__ represents a link between __Pool__ and __HealthCheck__.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_check_id** | **str** | The resource identifier. | 
**name** | **str** | Display name of __HealthCheck__. | [optional] [readonly] 

## Example

```python
from dtc.models.pool_health_check import PoolHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of PoolHealthCheck from a JSON string
pool_health_check_instance = PoolHealthCheck.from_json(json)
# print the JSON string representation of the object
print(PoolHealthCheck.to_json())

# convert the object into a dict
pool_health_check_dict = pool_health_check_instance.to_dict()
# create an instance of PoolHealthCheck from a dict
pool_health_check_from_dict = PoolHealthCheck.from_dict(pool_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


