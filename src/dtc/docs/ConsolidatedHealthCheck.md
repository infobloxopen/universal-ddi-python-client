# ConsolidatedHealthCheck

When set, the DNS server running the named designator __DNS Service__ performs the health check on behalf of the __Pool__, and the result is shared with other DNS servers linked to the __Pool__ via __LBDN__ association. When unset, each DNS server performs the health check independently and no health status is shared.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**designators** | [**List[DesignatorService]**](DesignatorService.md) | Designator __DNS Service__ references where the corresponding health checks will be associated to. Must contain at least one entry when set.  On request: only _dns_service_id_ is honoured. On response: _dns_service_name_ is echoed alongside, resolved from inventory. | [optional] 

## Example

```python
from dtc.models.consolidated_health_check import ConsolidatedHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ConsolidatedHealthCheck from a JSON string
consolidated_health_check_instance = ConsolidatedHealthCheck.from_json(json)
# print the JSON string representation of the object
print(ConsolidatedHealthCheck.to_json())

# convert the object into a dict
consolidated_health_check_dict = consolidated_health_check_instance.to_dict()
# create an instance of ConsolidatedHealthCheck from a dict
consolidated_health_check_from_dict = ConsolidatedHealthCheck.from_dict(consolidated_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


