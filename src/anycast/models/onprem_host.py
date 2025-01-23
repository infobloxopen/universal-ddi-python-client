# coding: utf-8

"""
    Universal DDI Anycast API

    Anycast capability enables HA (High Availability) configuration of Universal DDI applications that run on equipment located on customer's premises (on-prem hosts). Anycast supports DNS, as well as DNS-forwarding services.  Anycast-enabled application setups use multiple on-premises installations for one particular application type. Multiple application instances are configured to use the same endpoint address. Anycast capability is collocated with such application instance, monitoring the local application instance and advertising to the upstream router (a customer equipment) a per-instance, local route to the common application endpoint address, as long as the local application instance is available. Depending on the type of the upstream router, the customer may configure local route advertisement via either BGP (Boarder Gateway Protocol) or OSPF (Open Shortest Path First) routing protocols. Both protocols may be enabled as well. Multiple routes to the common application service address provide redundancy without the need to reconfigure application clients.  Should an application instance become unavailable, the local route advertisements stop, resulting in withdrawal of the route (in the upstream router) to the application instance that has gone out of service and ensuring that subsequent application requests thus get routed to the remaining available application instances.  

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from anycast.models.anycast_config_ref import AnycastConfigRef
from anycast.models.bgp_config import BgpConfig
from anycast.models.ospf_config import OspfConfig
from anycast.models.ospfv3_config import Ospfv3Config
from typing import Optional, Set
from typing_extensions import Self


class OnpremHost(BaseModel):
    """
    OnpremHost
    """

  # noqa: E501
    anycast_config_refs: Optional[List[AnycastConfigRef]] = None
    config_bgp: Optional[BgpConfig] = None
    config_ospf: Optional[OspfConfig] = None
    config_ospfv3: Optional[Ospfv3Config] = None
    created_at: Optional[datetime] = None
    id: Optional[StrictInt] = None
    ip_address: Optional[StrictStr] = Field(
        default=None, description="IPv4 address of the on-prem host")
    ipv6_address: Optional[StrictStr] = Field(
        default=None, description="IPv6 address of the on-prem host")
    name: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "anycast_config_refs", "config_bgp", "config_ospf", "config_ospfv3",
        "created_at", "id", "ip_address", "ipv6_address", "name", "updated_at"
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
        """Create an instance of OnpremHost from a JSON string"""
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
            "id",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in anycast_config_refs (list)
        _items = []
        if self.anycast_config_refs:
            for _item in self.anycast_config_refs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['anycast_config_refs'] = _items
        # override the default output from pydantic by calling `to_dict()` of config_bgp
        if self.config_bgp:
            _dict['config_bgp'] = self.config_bgp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_ospf
        if self.config_ospf:
            _dict['config_ospf'] = self.config_ospf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_ospfv3
        if self.config_ospfv3:
            _dict['config_ospfv3'] = self.config_ospfv3.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OnpremHost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anycast_config_refs": [
                AnycastConfigRef.from_dict(_item)
                for _item in obj["anycast_config_refs"]
            ] if obj.get("anycast_config_refs") is not None else None,
            "config_bgp":
            BgpConfig.from_dict(obj["config_bgp"])
            if obj.get("config_bgp") is not None else None,
            "config_ospf":
            OspfConfig.from_dict(obj["config_ospf"])
            if obj.get("config_ospf") is not None else None,
            "config_ospfv3":
            Ospfv3Config.from_dict(obj["config_ospfv3"])
            if obj.get("config_ospfv3") is not None else None,
            "created_at":
            obj.get("created_at"),
            "id":
            obj.get("id"),
            "ip_address":
            obj.get("ip_address"),
            "ipv6_address":
            obj.get("ipv6_address"),
            "name":
            obj.get("name"),
            "updated_at":
            obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
