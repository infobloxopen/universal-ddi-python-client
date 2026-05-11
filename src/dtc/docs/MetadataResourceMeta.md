# MetadataResourceMeta

Limited view on a configuration resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **Dict[str, str]** | Structured data consisting of additional details of the configuration resource. | [optional] 
**display_name** | **str** | Display name of the configuration resource. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 

## Example

```python
from dtc.models.metadata_resource_meta import MetadataResourceMeta

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataResourceMeta from a JSON string
metadata_resource_meta_instance = MetadataResourceMeta.from_json(json)
# print the JSON string representation of the object
print(MetadataResourceMeta.to_json())

# convert the object into a dict
metadata_resource_meta_dict = metadata_resource_meta_instance.to_dict()
# create an instance of MetadataResourceMeta from a dict
metadata_resource_meta_from_dict = MetadataResourceMeta.from_dict(metadata_resource_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


