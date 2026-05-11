# Policy

A __Policy__ (_dtc/policy_) represents a DNS load balancing policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __Policy__. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __Policy__.  Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_sources** | [**TTLInheritance**](TTLInheritance.md) | Optional. The inheritance configuration. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __Policy__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**method** | **str** | Load balancing method used for selecting __Pool__ assigned to __Policy__.  Valid values are: * _round_robin_ If the _round_robin_ load balancing method is selected, BloxOne DDI adjusts the response to a query in a sequential and circular manner, directing clients to pools.  * _ratio_ If _ratio_ load balancing method is selected, BloxOne DDI adjusts the response to a query so that clients are directed to pool using weighted round robin, a load-balancing pattern in which requests are distributed among several resources based on weight assigned to each resource. The distribution of responses over time will be equal for all available pools but the sequence of the responses won&#39;t be guaranteed. When equal weights are assigned for resources (pools) it effectively leads to basic round robin configuration which directs clients to pools in a sequential and circular manner.  * _topology_ If _topology_ load balancing method is selected the pools configured for the policy are ignored and topology rules are used instead.  * _global_availability_ If _global_availability_ load balancing method is selected clients are directed to the first pool that is up in the _pools_ list.  Defaults to _round_robin_. | 
**name** | **str** | Display name of __Policy__. | 
**pools** | [**List[PolicyPool]**](PolicyPool.md) | Optional. List of __Pool__ objects assigned to __Policy__.  Defaults to _empty_. | [optional] 
**rules** | [**List[TopologyRule]**](TopologyRule.md) | Optional. List of __TopologyRule__ objects defining the resolving strategy for __Policy__.  Defaults to a list of single, default __TopologyRule__. | [optional] 
**tags** | **object** | Optional. The tags for __Policy__ in JSON format. | [optional] 
**ttl** | **int** | Optional. Time to live value (in seconds) to be used for records in DTC response. Unsigned integer, min: 0, max 2147483647 (31-bits per RFC-2181). | [optional] 

## Example

```python
from dtc.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print(Policy.to_json())

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_from_dict = Policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


