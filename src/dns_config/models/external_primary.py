# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

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
from dns_config.models.tsig_key import TSIGKey
from typing import Optional, Set
from typing_extensions import Self


class ExternalPrimary(BaseModel):
    """
    External DNS primary.
    """

  # noqa: E501
    address: Optional[StrictStr] = Field(
        default=None,
        description=
        "Optional. Required only if _type_ is _server_. IP Address of nameserver."
    )
    fqdn: Optional[StrictStr] = Field(
        default=None,
        description=
        "Optional. Required only if _type_ is _server_. FQDN of nameserver.")
    nsg: Optional[StrictStr] = Field(default=None,
                                     description="The resource identifier.")
    protocol_fqdn: Optional[StrictStr] = Field(
        default=None, description="FQDN of nameserver in punycode.")
    tsig_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary."
    )
    tsig_key: Optional[TSIGKey] = Field(
        default=None,
        description=
        "Optional. TSIG key.  Error if empty while _tsig_enabled_ is _true_.")
    type: StrictStr = Field(
        description="Allowed values: * _nsg_, * _primary_.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "address", "fqdn", "nsg", "protocol_fqdn", "tsig_enabled", "tsig_key",
        "type"
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
        """Create an instance of ExternalPrimary from a JSON string"""
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
            "protocol_fqdn",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
        """Create an instance of ExternalPrimary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address":
            obj.get("address"),
            "fqdn":
            obj.get("fqdn"),
            "nsg":
            obj.get("nsg"),
            "protocol_fqdn":
            obj.get("protocol_fqdn"),
            "tsig_enabled":
            obj.get("tsig_enabled"),
            "tsig_key":
            TSIGKey.from_dict(obj["tsig_key"])
            if obj.get("tsig_key") is not None else None,
            "type":
            obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
