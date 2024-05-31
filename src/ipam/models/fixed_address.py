# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.fixed_address_inheritance import FixedAddressInheritance
from ipam.models.inheritance_assigned_host import InheritanceAssignedHost
from ipam.models.option_item import OptionItem
from typing import Optional, Set
from typing_extensions import Self


class FixedAddress(BaseModel):
    """
    A __FixedAddress__ object (_dhcp/fixed_address_) reserves an address for a specific client. It must have a _match_type_ and a valid corresponding _match_value_ so it can match that client.
    """ # noqa: E501
    address: StrictStr = Field(description="The reserved address.")
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the fixed address. May contain 0 to 1024 characters. Can include UTF-8."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    dhcp_options: Optional[List[OptionItem]] = Field(
        default=None,
        description=
        "The list of DHCP options. May be either a specific option or a group of options."
    )
    disable_dhcp: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to disable object. The fixed address is converted to an exclusion when generating configuration.  Defaults to _false_."
    )
    header_option_filename: Optional[StrictStr] = Field(
        default=None,
        description="The configuration for header option filename field.")
    header_option_server_address: Optional[StrictStr] = Field(
        default=None,
        description="The configuration for header option server address field."
    )
    header_option_server_name: Optional[StrictStr] = Field(
        default=None,
        description="The configuration for header option server name field.")
    hostname: Optional[StrictStr] = Field(
        default=None,
        description=
        "The DHCP host name associated with this fixed address. It is of FQDN type and it defaults to empty."
    )
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    inheritance_assigned_hosts: Optional[List[InheritanceAssignedHost]] = Field(
        default=None,
        description="The list of the inheritance assigned hosts of the object."
    )
    inheritance_parent: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    inheritance_sources: Optional[FixedAddressInheritance] = Field(
        default=None, description="The inheritance configuration.")
    ip_space: Optional[StrictStr] = Field(
        default=None, description="The resource identifier.")
    match_type: StrictStr = Field(
        description=
        "Indicates how to match the client:  * _mac_: match the client MAC address for both IPv4 and IPv6,  * _client_text_ or _client_hex_: match the client identifier for IPv4 only,  * _relay_text_ or _relay_hex_: match the circuit ID or remote ID in the DHCP relay agent option (82) for IPv4 only,  * _duid_: match the DHCP unique identifier, currently match only for IPv6 protocol."
    )
    match_value: StrictStr = Field(description="The value to match.")
    name: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the fixed address. May contain 1 to 256 characters. Can include UTF-8."
    )
    parent: Optional[StrictStr] = Field(default=None,
                                        description="The resource identifier.")
    tags: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The tags for the fixed address in JSON format.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "address", "comment", "created_at", "dhcp_options", "disable_dhcp",
        "header_option_filename", "header_option_server_address",
        "header_option_server_name", "hostname", "id",
        "inheritance_assigned_hosts", "inheritance_parent",
        "inheritance_sources", "ip_space", "match_type", "match_value", "name",
        "parent", "tags", "updated_at"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FixedAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "id",
            "inheritance_assigned_hosts",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in dhcp_options (list)
        _items = []
        if self.dhcp_options:
            for _item in self.dhcp_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dhcp_options'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inheritance_assigned_hosts (list)
        _items = []
        if self.inheritance_assigned_hosts:
            for _item in self.inheritance_assigned_hosts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inheritance_assigned_hosts'] = _items
        # override the default output from pydantic by calling `to_dict()` of inheritance_sources
        if self.inheritance_sources:
            _dict['inheritance_sources'] = self.inheritance_sources.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FixedAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address":
            obj.get("address"),
            "comment":
            obj.get("comment"),
            "created_at":
            obj.get("created_at"),
            "dhcp_options":
            [OptionItem.from_dict(_item) for _item in obj["dhcp_options"]]
            if obj.get("dhcp_options") is not None else None,
            "disable_dhcp":
            obj.get("disable_dhcp"),
            "header_option_filename":
            obj.get("header_option_filename"),
            "header_option_server_address":
            obj.get("header_option_server_address"),
            "header_option_server_name":
            obj.get("header_option_server_name"),
            "hostname":
            obj.get("hostname"),
            "id":
            obj.get("id"),
            "inheritance_assigned_hosts": [
                InheritanceAssignedHost.from_dict(_item)
                for _item in obj["inheritance_assigned_hosts"]
            ] if obj.get("inheritance_assigned_hosts") is not None else None,
            "inheritance_parent":
            obj.get("inheritance_parent"),
            "inheritance_sources":
            FixedAddressInheritance.from_dict(obj["inheritance_sources"])
            if obj.get("inheritance_sources") is not None else None,
            "ip_space":
            obj.get("ip_space"),
            "match_type":
            obj.get("match_type"),
            "match_value":
            obj.get("match_value"),
            "name":
            obj.get("name"),
            "parent":
            obj.get("parent"),
            "tags":
            obj.get("tags"),
            "updated_at":
            obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
