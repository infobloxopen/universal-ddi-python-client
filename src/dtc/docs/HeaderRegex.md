# HeaderRegex

A __HeaderRegex__ represents a pair of HTTP header name and regular expression to match against the header value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** | HTTP header name. | 
**regex** | **str** | Regular expression to match against HTTP header value. | 

## Example

```python
from dtc.models.header_regex import HeaderRegex

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderRegex from a JSON string
header_regex_instance = HeaderRegex.from_json(json)
# print the JSON string representation of the object
print(HeaderRegex.to_json())

# convert the object into a dict
header_regex_dict = header_regex_instance.to_dict()
# create an instance of HeaderRegex from a dict
header_regex_from_dict = HeaderRegex.from_dict(header_regex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


