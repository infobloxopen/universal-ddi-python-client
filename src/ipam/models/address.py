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
from ipam.models.dhcp_info import DHCPInfo
from ipam.models.name import Name
from typing import Optional, Set
from typing_extensions import Self


class Address(BaseModel):
    """
    An __Address__ object (_ipam/address_) represents any single IP address within a given IP space.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(
        default=None,
        description="The address in form \"a.b.c.d\"."
    )
    comment: Optional[StrictStr] = Field(
        default=None,
        description=
        "The description for the address object. May contain 0 to 1024 characters. Can include UTF-8."
    )
    compartment_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    dhcp_info: Optional[DHCPInfo] = Field(
        default=None,
        description="The DHCP information associated with this object.")
    disable_dhcp: Optional[StrictBool] = Field(
        default=None,
        description=
        "Read only. Represent the value of the same field in the associated _dhcp/fixed_address_ object."
    )
    discovery_attrs: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The discovery attributes for this address in JSON format."
    )
    discovery_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="The discovery metadata for this address in JSON format.")
    external_keys: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        "The external keys (source key) for this address in JSON format.")
    host: Optional[StrictStr] = Field(default=None,
                                      description="The resource identifier.")
    hwaddr: Optional[StrictStr] = Field(
        default=None,
        description="The hardware address associated with this IP address.")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    interface: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of the network interface card (NIC) associated with the address, if any."
    )
    names: Optional[List[Name]] = Field(
        default=None,
        description="The list of all names associated with this address.")
    parent: Optional[StrictStr] = Field(default=None,
                                        description="The resource identifier.")
    protocol: Optional[StrictStr] = Field(
        default=None, description="The type of protocol (_ip4_ or _ip6_).")
    range: Optional[StrictStr] = Field(default=None,
                                       description="The resource identifier.")
    space: Optional[StrictStr] = Field(default=None,
                                       description="The resource identifier.")
    state: Optional[StrictStr] = Field(
        default=None,
        description="The state of the address (_used_ or _free_).")
    tags: Optional[Dict[str, Any]] = Field(
        default=None, description="The tags for this address in JSON format.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    usage: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:  usage indicator        | description  ---------------------- | --------------------------------  _IPAM_                 |  Address was created by the IPAM component.  _IPAM_, _RESERVED_     |  Address was created by the API call _ipam/address_ or _ipam/host_.  _IPAM_, _NETWORK_      |  Address was automatically created by the IPAM component and is the network address of the parent subnet.  _IPAM_, _BROADCAST_    |  Address was automatically created by the IPAM component and is the broadcast address of the parent subnet.  _DHCP_                 |  Address was created by the DHCP component.  _DHCP_, _FIXEDADDRESS_ |  Address was created by the API call _dhcp/fixed_address_.  _DHCP_, _LEASED_       |  An active lease for that address was issued by a DHCP server.  _DHCP_, _DISABLED_     |  Address is disabled.  _DNS_                  |  Address is used by one or more DNS records.  _DISCOVERED_           |  Address is discovered by some network discovery probe like Network Insight or NetMRI in NIOS."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "address", "comment", "compartment_id", "created_at", "dhcp_info",
        "disable_dhcp", "discovery_attrs", "discovery_metadata",
        "external_keys", "host", "hwaddr", "id", "interface", "names",
        "parent", "protocol", "range", "space", "state", "tags", "updated_at",
        "usage"
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
        """Create an instance of Address from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "compartment_id",
            "created_at",
            "dhcp_info",
            "disable_dhcp",
            "discovery_attrs",
            "discovery_metadata",
            "id",
            "protocol",
            "state",
            "updated_at",
            "usage",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dhcp_info
        if self.dhcp_info:
            _dict['dhcp_info'] = self.dhcp_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in names (list)
        _items = []
        if self.names:
            for _item in self.names:
                if _item:
                    _items.append(_item.to_dict())
            _dict['names'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address":
            obj.get("address"),
            "comment":
            obj.get("comment"),
            "compartment_id":
            obj.get("compartment_id"),
            "created_at":
            obj.get("created_at"),
            "dhcp_info":
            DHCPInfo.from_dict(obj["dhcp_info"])
            if obj.get("dhcp_info") is not None else None,
            "disable_dhcp":
            obj.get("disable_dhcp"),
            "discovery_attrs":
            obj.get("discovery_attrs"),
            "discovery_metadata":
            obj.get("discovery_metadata"),
            "external_keys":
            obj.get("external_keys"),
            "host":
            obj.get("host"),
            "hwaddr":
            obj.get("hwaddr"),
            "id":
            obj.get("id"),
            "interface":
            obj.get("interface"),
            "names": [Name.from_dict(_item) for _item in obj["names"]]
            if obj.get("names") is not None else None,
            "parent":
            obj.get("parent"),
            "protocol":
            obj.get("protocol"),
            "range":
            obj.get("range"),
            "space":
            obj.get("space"),
            "state":
            obj.get("state"),
            "tags":
            obj.get("tags"),
            "updated_at":
            obj.get("updated_at"),
            "usage":
            obj.get("usage")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
