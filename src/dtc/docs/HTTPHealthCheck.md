# HTTPHealthCheck

A __HTTPHealthCheck__ (_dtc/health_check_http_) represents a DTC __Server__ health check based on the Hypertext Transfer Protocol (HTTP).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_response_body** | **bool** | Optional. Flag which enables checking of the HTTP response body content. Defaults to _false_. | [optional] 
**check_response_body_negative** | **bool** | Optional. Flag which changes the meaning of the regex match result. If set to _true_, the response is valid if regular expression matches not found. Defaults to _false_.  The flag is currently not supported. | [optional] 
**check_response_body_regex** | **str** | Optional. Regular expression to search for a string in the HTTP response body. Error if empty while _check_response_body_ is _true_. Defaults to empty. | [optional] 
**check_response_header** | **bool** | Optional. Flag which enables checking of the HTTP response header(s) content. Defaults to _false_. | [optional] 
**check_response_header_negative** | **bool** | Optional. Flag which changes the meaning of the header regexes match result. If set to _true_, neither expression matches must be found in their respective headers for the headers to be considered valid. Defaults to _false_. | [optional] 
**check_response_header_regexes** | [**List[HeaderRegex]**](HeaderRegex.md) | Optional. List of (header, regular expression) pairs. All expression matches must be found in their respective headers for the headers to be considered valid. Error if empty while _check_response_header_ is _true_. Defaults to empty. | [optional] 
**codes** | **str** | Optional. Response Status Codes meaning the health check is successful. If empty, any code means success. Individual codes and code ranges are supported, ex. \&quot;102,105-107,109-110,120\&quot;. | [optional] 
**comment** | **str** | Optional. Comment for __HTTPHealthCheck__. | [optional] 
**disabled** | **bool** | Optional. Flag which enables/disables __HTTPHealthCheck__. Defaults to _false_. | [optional] 
**https** | **bool** | Optional. Flag which enables Hypertext Transfer Protocol Secure (HTTPS) in a health check. Defaults to _false_. | [optional] 
**id** | **str** | The resource identifier. | [optional] [readonly] 
**interval** | **int** | Optional. Interval value in seconds. The health check runs only for the specified interval and it is measured from the beginning of the previous check cycle. Defaults to _15_. | [optional] 
**metadata** | [**Metadata**](Metadata.md) | Output only. __HTTPHealthCheck__ metadata. Defaults to empty object and should be explicitly requested using field selection. | [optional] 
**name** | **str** | Display name of __HTTPHealthCheck__. | 
**port** | **int** | Destination TCP port of __HTTPHealthCheck__. | 
**request** | **str** | HTTP request in a text format, it consists of HTTP method, request target, HTTP headers, request body. | [optional] 
**retry_down** | **int** | Optional. Retry down count. The value determines how many bad health checks in a row must be received by the onprem host from the DTC Server for treating the health check as failed. Defaults to _1_. | [optional] 
**retry_up** | **int** | Optional. Retry up count. The value determines how many good health checks in a row must be received by the onprem host from the DTC Server for treating the health check as successful. Defaults to _1_. | [optional] 
**tags** | **object** | Optional. The tags for __HTTPHealthCheck__ in JSON format. | [optional] 
**timeout** | **int** | Optional. Timeout value in seconds. The health check waits for the specified number of seconds after sending a request. If it does not receive a response within the number of seconds, then the health check is considered as failed. Defaults to _10_. | [optional] 

## Example

```python
from dtc.models.http_health_check import HTTPHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPHealthCheck from a JSON string
http_health_check_instance = HTTPHealthCheck.from_json(json)
# print the JSON string representation of the object
print(HTTPHealthCheck.to_json())

# convert the object into a dict
http_health_check_dict = http_health_check_instance.to_dict()
# create an instance of HTTPHealthCheck from a dict
http_health_check_from_dict = HTTPHealthCheck.from_dict(http_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


