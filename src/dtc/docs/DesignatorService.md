# DesignatorService

Reference to a __DNS Service__ that acts as a designator for a __ConsolidatedHealthCheck__.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_service_id** | **str** | The resource identifier. | 
**dns_service_name** | **str** | Display name of the __DNS Service__. Response-only; ignored on request. | [optional] [readonly] 

## Example

```python
from dtc.models.designator_service import DesignatorService

# TODO update the JSON string below
json = "{}"
# create an instance of DesignatorService from a JSON string
designator_service_instance = DesignatorService.from_json(json)
# print the JSON string representation of the object
print(DesignatorService.to_json())

# convert the object into a dict
designator_service_dict = designator_service_instance.to_dict()
# create an instance of DesignatorService from a dict
designator_service_from_dict = DesignatorService.from_dict(designator_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


