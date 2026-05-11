# SNMPHealthCheck

A __SNMPHealthCheck__ (_dtc/health_check_snmp_) represents a DTC __Server__ health check based on the Simple Network Management Protocol (SNMP).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_list** | [**List[SNMPHealthCheckEntryCheck]**](SNMPHealthCheckEntryCheck.md) | List of specific checks for SNMP entries and their values in MIB hierarchy. Supported up to 15 checks. | [optional] 
**comment** | **str** | Optional. Comment for __SNMPHealthCheck__. | [optional] 
**community** | **str** | Optional. SNMP community string used for authentication. Mandatory for __v1__ and __v2c__ versions, ignored for __v3__.  Defaults to __public__. | [optional] 
**context_engine_id** | **str** | Optional. Uniquely identifies an SNMP entity that may realize an instance of a context with a particular context name.  Format is an arbitrary string that can contain from 10 to 64 hexadecimal digits (5 to 32 octet numbers).  Ignored for __v1__ and __v2c__ versions. | [optional] 
**context_name** | **str** | Optional. Name of administratively unique context for __v3__ version. Ignored for __v1__ and __v2c__ versions. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __SNMPHealthCheck__. Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interval** | **int** | Optional. Interval value in seconds. The health check runs only for the specified interval and it is measured from the beginning of the previous check cycle. Defaults to _15_. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __SNMPHealthCheck__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**name** | **str** | Display name of __SNMPHealthCheck__. | 
**port** | **int** | Optional. Destination UDP port of __SNMPHealthCheck__. Defaults to _161_. | [optional] 
**retry_down** | **int** | Optional. Retry down count. The value determines how many bad health checks in a row must be received by the onprem host from the DTC Server for treating the health check as failed. Defaults to _1_. | [optional] 
**retry_up** | **int** | Optional. Retry up count. The value determines how many good health checks in a row must be received by the onprem host from the DTC Server for treating the health check as successful. Defaults to _1_. | [optional] 
**tags** | **object** | Optional. The tags for __SNMPHealthCheck__ in JSON format. | [optional] 
**timeout** | **int** | Optional. Timeout value in seconds. The health check waits for the specified number of seconds after sending a request. If it does not receive a response within the number of seconds, then the health check is considered as failed. Defaults to _10_. | [optional] 
**user_security_model** | **str** | The resource identifier. | [optional] 
**version** | **str** | SNMP version.  Allowed values: * v1  - version 1 * v2c - version 2 community * v3  - version 3 | 

## Example

```python
from dtc.models.snmp_health_check import SNMPHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of SNMPHealthCheck from a JSON string
snmp_health_check_instance = SNMPHealthCheck.from_json(json)
# print the JSON string representation of the object
print(SNMPHealthCheck.to_json())

# convert the object into a dict
snmp_health_check_dict = snmp_health_check_instance.to_dict()
# create an instance of SNMPHealthCheck from a dict
snmp_health_check_from_dict = SNMPHealthCheck.from_dict(snmp_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


