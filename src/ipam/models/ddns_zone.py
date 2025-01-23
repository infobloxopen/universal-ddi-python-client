# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a Universal DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.nameserver import Nameserver
from ipam.models.tsig_key import TSIGKey
from typing import Optional, Set
from typing_extensions import Self


class DDNSZone(BaseModel):
    """
    A __DDNSZone__ object (_dhcp/ddns_zone_) represents a DNS zone that can accept dynamic DNS updates from DHCP.
    """ # noqa: E501
    fqdn: Optional[StrictStr] = Field(
        default=None,
        description=
        "Zone FQDN.  If _zone_ is defined, the _fqdn_ field must be empty.")
    gss_tsig_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "_gss_tsig_enabled_ enables/disables GSS-TSIG signed dynamic updates.  Defaults to _false_."
    )
    nameservers: Optional[List[Nameserver]] = Field(
        default=None,
        description=
        "The Nameservers in the zone.  Each nameserver IP should be unique across the list of nameservers."
    )
    tsig_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Indicates if TSIG key should be used for the update.  Defaults to _false_."
    )
    tsig_key: Optional[TSIGKey] = Field(
        default=None,
        description=
        "The TSIG key. Required if _tsig_enabled_ is _true_.  Defaults to empty."
    )
    view: Optional[StrictStr] = Field(default=None,
                                      description="The resource identifier.")
    view_name: Optional[StrictStr] = Field(default=None,
                                           description="The name of the view.")
    zone: StrictStr = Field(description="The resource identifier.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "fqdn", "gss_tsig_enabled", "nameservers", "tsig_enabled", "tsig_key",
        "view", "view_name", "zone"
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
        """Create an instance of DDNSZone from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "view_name",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in nameservers (list)
        _items = []
        if self.nameservers:
            for _item in self.nameservers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nameservers'] = _items
        # override the default output from pydantic by calling `to_dict()` of tsig_key
        if self.tsig_key:
            _dict['tsig_key'] = self.tsig_key.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DDNSZone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fqdn":
            obj.get("fqdn"),
            "gss_tsig_enabled":
            obj.get("gss_tsig_enabled"),
            "nameservers":
            [Nameserver.from_dict(_item) for _item in obj["nameservers"]]
            if obj.get("nameservers") is not None else None,
            "tsig_enabled":
            obj.get("tsig_enabled"),
            "tsig_key":
            TSIGKey.from_dict(obj["tsig_key"])
            if obj.get("tsig_key") is not None else None,
            "view":
            obj.get("view"),
            "view_name":
            obj.get("view_name"),
            "zone":
            obj.get("zone")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
