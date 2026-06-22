# Pool

A __Pool__ (_dtc/pool_) represents a collection of servers, it is associated with a __Policy__ (_dtc/policy_).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional. Comment for __Pool__. | [optional] 
**consolidated_health_enabled** | **bool** | Optional. Pool-level switch that enables consolidated health probing for this __Pool__.  Defaults to _false_ (consolidated health disabled). Set to _true_ to enable consolidated probing on this __Pool__. When _false_, any per-__PoolHealthCheck__ consolidation configuration is preserved in storage but suppressed at runtime. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __Pool__.  Defaults to _false_. | [optional] 
**health_checks** | [**List[PoolHealthCheck]**](PoolHealthCheck.md) | Optional. List of __HealthCheck__ objects IDs assigned to __Pool__.  Defaults to _empty_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**inheritance_sources** | [**TTLInheritance**](TTLInheritance.md) | Optional. The inheritance configuration. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __Pool__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**method** | **str** | Load balancing method used for selecting __Server__ assigned to __Pool__.  Valid values are: * _round_robin_ If the _round_robin_ load balancing method is selected, Universal DDI adjusts the response to a query in a sequential and circular manner, directing clients to pools.  * _ratio_ If _ratio_ load balancing method is selected, Universal DDI adjusts the response to a query so that clients are directed to pool using weighted round robin, a load-balancing pattern in which requests are distributed among several resources based on weight assigned to each resource. The distribution of responses over time will be equal for all available pools but the sequence of the responses won&#39;t be guaranteed. When equal weights are assigned for resources (pools) it effectively leads to basic round robin which directs clients to pools in sequential and circular manner.  * _global_availability_ If _global_availability_ load balancing method is selected clients are directed to the first server that is up in the _servers_ list.  Defaults to _round_robin_. | 
**name** | **str** | Display name of __Pool__. | 
**pool_availability** | **str** | Optional. Pool Availability setting defines how __Pool__ health is calculated.  Valid values are: * _all_ If _all_ availability selected then __Pool__ is treated healthy when all pool&#39;s servers are healthy. * _quorum_ If _quorum_ availability selected then __Pool__ is treated healthy when at least N pool&#39;s servers are healthy. N is configurable via the value from _pool_servers_quorum_ setting. * _any_ If _any_ availability selected then __Pool__ is treated healthy when at least one pool&#39;s server is healthy.  Defaults to _any_. | [optional] 
**pool_servers_quorum** | **int** | Pool Servers Quorum defines a minimal number of pool&#39;s healthy servers required for treating __Pool__ as healthy when Pool Availability is set to _quorum_. | [optional] 
**server_availability** | **str** | Optional. Server Availability setting defines how __Server__ health is calculated.  Valid values are: * _all_ If _all_ availability selected then __Server__ is treated healthy when all pool&#39;s health checks are positive. * _quorum_ If _quorum_ availability selected then __Server__ is treated healthy when at least N pool&#39;s health checks are positive. N is configurable via the value from _server_health_checks_quorum_ setting. * _any_ If _any_ availability selected then __Server__ is treated healthy when at least one pool&#39;s health check is positive  Defaults to _all_. | [optional] 
**server_health_checks_quorum** | **int** | Server Health Checks Quorum defines a minimal number of pool&#39;s positive health checks required for treating __Server__ as healthy when Server Availability is set to _quorum_. | [optional] 
**servers** | [**List[PoolServer]**](PoolServer.md) | Optional. List of __Server__ objects assigned to __Pool__.  Defaults to _empty_. | [optional] 
**tags** | **object** | Optional. The tags for __Pool__ in JSON format. | [optional] 
**ttl** | **int** | Optional. Time to live value (in seconds) to be used for records in DTC response. Unsigned integer, min: 0, max 2147483647 (31-bits per RFC-2181). | [optional] 

## Example

```python
from dtc.models.pool import Pool

# TODO update the JSON string below
json = "{}"
# create an instance of Pool from a JSON string
pool_instance = Pool.from_json(json)
# print the JSON string representation of the object
print(Pool.to_json())

# convert the object into a dict
pool_dict = pool_instance.to_dict()
# create an instance of Pool from a dict
pool_from_dict = Pool.from_dict(pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


