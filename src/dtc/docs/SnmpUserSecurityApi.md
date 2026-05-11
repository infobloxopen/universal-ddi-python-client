# dtc.SnmpUserSecurityApi

All URIs are relative to *http://localhost/api/ddi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SnmpUserSecurityApi.md#create) | **POST** /dtc/snmp_user_security_model | Create the SNMPUserSecurityModel object. Use this method to create a __SNMPUserSecurityModel__ object.
[**delete**](SnmpUserSecurityApi.md#delete) | **DELETE** /dtc/snmp_user_security_model/{id} | Delete the SNMPUserSecurityModel object. Use this method to delete a __SNMPUserSecurityModel__ object.
[**list**](SnmpUserSecurityApi.md#list) | **GET** /dtc/snmp_user_security_model | Retrieve SNMPUserSecurityModel objects. Use this method to retrieve __SNMPUserSecurityModel__ objects.
[**read**](SnmpUserSecurityApi.md#read) | **GET** /dtc/snmp_user_security_model/{id} | Retrieve the SNMPUserSecurityModel object. Use this method to retrieve a __SNMPUserSecurityModel__ object.
[**update**](SnmpUserSecurityApi.md#update) | **PATCH** /dtc/snmp_user_security_model/{id} | Update the SNMPUserSecurityModel object. Use this method to update a __SNMPUserSecurityModel__ object.


# **create**
> CreateSNMPUserSecurityResponse create(body)

Create the SNMPUserSecurityModel object. Use this method to create a __SNMPUserSecurityModel__ object.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dtc

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtc.SnmpUserSecurityApi(api_client)
    body = dtc.SNMPUserSecurityModel() # SNMPUserSecurityModel | 

    try:
        # Create the SNMPUserSecurityModel object. Use this method to create a __SNMPUserSecurityModel__ object.
        api_response = api_instance.create(body)
        pprint("The response of SnmpUserSecurityApi->create:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling SnmpUserSecurityApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SNMPUserSecurityModel**](SNMPUserSecurityModel.md)|  | 

### Return type

[**CreateSNMPUserSecurityResponse**](CreateSNMPUserSecurityResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | POST operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete the SNMPUserSecurityModel object. Use this method to delete a __SNMPUserSecurityModel__ object.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dtc

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtc.SnmpUserSecurityApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Delete the SNMPUserSecurityModel object. Use this method to delete a __SNMPUserSecurityModel__ object.
        api_instance.delete(id)
    except Exception as e:
        pprint("Exception when calling SnmpUserSecurityApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListSNMPUserSecurityResponse list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by)

Retrieve SNMPUserSecurityModel objects. Use this method to retrieve __SNMPUserSecurityModel__ objects.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dtc

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtc.SnmpUserSecurityApi(api_client)

    try:
        # Retrieve SNMPUserSecurityModel objects. Use this method to retrieve __SNMPUserSecurityModel__ objects.
        api_response = api_instance.list()
        pprint("The response of SnmpUserSecurityApi->list:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling SnmpUserSecurityApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 

### Return type

[**ListSNMPUserSecurityResponse**](ListSNMPUserSecurityResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> ReadSNMPUserSecurityResponse read(id, fields=fields)

Retrieve the SNMPUserSecurityModel object. Use this method to retrieve a __SNMPUserSecurityModel__ object.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dtc

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtc.SnmpUserSecurityApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource

    try:
        # Retrieve the SNMPUserSecurityModel object. Use this method to retrieve a __SNMPUserSecurityModel__ object.
        api_response = api_instance.read(id)
        pprint("The response of SnmpUserSecurityApi->read:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling SnmpUserSecurityApi->read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**ReadSNMPUserSecurityResponse**](ReadSNMPUserSecurityResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GET operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> UpdateSNMPUserSecurityResponse update(id, body)

Update the SNMPUserSecurityModel object. Use this method to update a __SNMPUserSecurityModel__ object.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import os
from pprint import pprint

import dtc

from universal_ddi_client.api_client import ApiClient
from universal_ddi_client.configuration import Configuration

# Defining the Portal URL is optional and defaults to "https://csp.infoblox.com"
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration(
    portal_url = os.getenv('INFOBLOX_PORTAL_URL'),
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

# Configure Portal key authorization: ApiKeyAuth
configuration.portal_key = os.getenv("INFOBLOX_PORTAL_KEY")

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtc.SnmpUserSecurityApi(api_client)
    id = 'id_example' # str | An application specific resource identity of a resource
    body = dtc.SNMPUserSecurityModel() # SNMPUserSecurityModel | 

    try:
        # Update the SNMPUserSecurityModel object. Use this method to update a __SNMPUserSecurityModel__ object.
        api_response = api_instance.update(id, body)
        pprint("The response of SnmpUserSecurityApi->update:\n")
        pprint(api_response)
    except Exception as e:
        pprint("Exception when calling SnmpUserSecurityApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**SNMPUserSecurityModel**](SNMPUserSecurityModel.md)|  | 

### Return type

[**UpdateSNMPUserSecurityResponse**](UpdateSNMPUserSecurityResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PATCH operation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

