# Server

An __Server__ (_dtc/server_) represents a target resource for load balancing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP Address of the __Server__. Must be set to a valid IP address if __endpoint_type__ is set to __address__. Alternatively, it can be left blank. | [optional] 
**auto_create_response_records** | **bool** | Optional. If the flag is enabled, A, AAAA or CNAME __Record__ is automatically generated.  Defaults to _false_. | [optional] 
**comment** | **str** | Optional. Comment for __Server__. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __Server__.  Defaults to _false_. | [optional] 
**endpoint_type** | **str** | The endpoint type configured for the __Server__. Can be IP Address or FQDN. The values of both fields __address__ and __fqdn__ are preserved and are not mutually exclusive, and the __endpoint_type__ defines which one to use.  Allowed values: * address * fqdn  Defaults to __address__. | [optional] 
**fqdn** | **str** | Fully Qualified Domain name of the __Server__. Must be set to a valid FQDN if __endpoint_type__ is set to __fqdn__. Alternatively, it can be left blank. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __Server__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**name** | **str** | Display name of __Server__. | 
**records** | [**List[Record]**](Record.md) | Optional. List of __Records__ of the __Server__. | [optional] 
**tags** | **object** | Optional. The tags for __Server__ in JSON format. | [optional] 

## Example

```python
from dtc.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_from_dict = Server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


