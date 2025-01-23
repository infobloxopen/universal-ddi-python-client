# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a Universal DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured Universal DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from dns_config.models.inheritance2_inherited_string import Inheritance2InheritedString
from dns_config.models.inheritance2_inherited_u_int32 import Inheritance2InheritedUInt32
from dns_config.models.inherited_zone_authority_m_name_block import InheritedZoneAuthorityMNameBlock
from typing import Optional, Set
from typing_extensions import Self


class InheritedZoneAuthority(BaseModel):
    """
    Inheritance configuration for a field of type _ZoneAuthority_.
    """ # noqa: E501
    default_ttl: Optional[Inheritance2InheritedUInt32] = Field(
        default=None,
        description=
        "Optional. Field config for _default_ttl_ field from _ZoneAuthority_ object."
    )
    expire: Optional[Inheritance2InheritedUInt32] = Field(
        default=None,
        description=
        "Optional. Field config for _expire_ field from _ZoneAuthority_ object."
    )
    mname_block: Optional[InheritedZoneAuthorityMNameBlock] = Field(
        default=None,
        description=
        "Optional. Field config for _mname_ block from _ZoneAuthority_ object."
    )
    negative_ttl: Optional[Inheritance2InheritedUInt32] = Field(
        default=None,
        description=
        "Optional. Field config for _negative_ttl_ field from _ZoneAuthority_ object."
    )
    protocol_rname: Optional[Inheritance2InheritedString] = Field(
        default=None,
        description=
        "Optional. Field config for _protocol_rname_ field from _ZoneAuthority_ object."
    )
    refresh: Optional[Inheritance2InheritedUInt32] = Field(
        default=None,
        description=
        "Optional. Field config for _refresh_ field from _ZoneAuthority_ object."
    )
    retry: Optional[Inheritance2InheritedUInt32] = Field(
        default=None,
        description=
        "Optional. Field config for _retry_ field from _ZoneAuthority_ object."
    )
    rname: Optional[Inheritance2InheritedString] = Field(
        default=None,
        description=
        "Optional. Field config for _rname_ field from _ZoneAuthority_ object."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "default_ttl", "expire", "mname_block", "negative_ttl",
        "protocol_rname", "refresh", "retry", "rname"
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
        """Create an instance of InheritedZoneAuthority from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of default_ttl
        if self.default_ttl:
            _dict['default_ttl'] = self.default_ttl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expire
        if self.expire:
            _dict['expire'] = self.expire.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mname_block
        if self.mname_block:
            _dict['mname_block'] = self.mname_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of negative_ttl
        if self.negative_ttl:
            _dict['negative_ttl'] = self.negative_ttl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of protocol_rname
        if self.protocol_rname:
            _dict['protocol_rname'] = self.protocol_rname.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refresh
        if self.refresh:
            _dict['refresh'] = self.refresh.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retry
        if self.retry:
            _dict['retry'] = self.retry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rname
        if self.rname:
            _dict['rname'] = self.rname.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InheritedZoneAuthority from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default_ttl":
            Inheritance2InheritedUInt32.from_dict(obj["default_ttl"])
            if obj.get("default_ttl") is not None else None,
            "expire":
            Inheritance2InheritedUInt32.from_dict(obj["expire"])
            if obj.get("expire") is not None else None,
            "mname_block":
            InheritedZoneAuthorityMNameBlock.from_dict(obj["mname_block"])
            if obj.get("mname_block") is not None else None,
            "negative_ttl":
            Inheritance2InheritedUInt32.from_dict(obj["negative_ttl"])
            if obj.get("negative_ttl") is not None else None,
            "protocol_rname":
            Inheritance2InheritedString.from_dict(obj["protocol_rname"])
            if obj.get("protocol_rname") is not None else None,
            "refresh":
            Inheritance2InheritedUInt32.from_dict(obj["refresh"])
            if obj.get("refresh") is not None else None,
            "retry":
            Inheritance2InheritedUInt32.from_dict(obj["retry"])
            if obj.get("retry") is not None else None,
            "rname":
            Inheritance2InheritedString.from_dict(obj["rname"])
            if obj.get("rname") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
