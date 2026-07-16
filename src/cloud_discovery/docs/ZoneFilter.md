# ZoneFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**wildcards** | **List[str]** |  | [optional] 

## Example

```python
from cloud_discovery.models.zone_filter import ZoneFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneFilter from a JSON string
zone_filter_instance = ZoneFilter.from_json(json)
# print the JSON string representation of the object
print(ZoneFilter.to_json())

# convert the object into a dict
zone_filter_dict = zone_filter_instance.to_dict()
# create an instance of ZoneFilter from a dict
zone_filter_from_dict = ZoneFilter.from_dict(zone_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


