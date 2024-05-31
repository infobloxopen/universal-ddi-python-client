# coding: utf-8

"""
    Infrastructure Management API

    The **Infrastructure Management API** provides a RESTful interface to manage Infrastructure Hosts and Services objects.  The following is a list of the different Services and their string types (the string types are to be used with the APIs for the `service_type` field):  | Service name | Service type |   | ------ | ------ |   | Access Authentication | authn |   | Anycast | anycast |   | Data Connector | cdc |   | DHCP | dhcp |   | DNS | dns |   | DNS Forwarding Proxy | dfp |   | NIOS Grid Connector | orpheus |   | MS AD Sync | msad |   | NTP | ntp |   | BGP | bgp |   | RIP | rip |   | OSPF | ospf |    ---   ### Hosts API  The Hosts API is used to manage the Infrastructure Host resources. These include various operations related to hosts such as viewing, creating, updating, replacing, disconnecting, and deleting Hosts. Management of Hosts is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Hosts tab.  ---   ### Services API  The Services API is used to manage the Infrastructure Service resources (a.k.a. BloxOne applications). These include various operations related to hosts such as viewing, creating, updating, starting/stopping, configuring, and deleting Services. Management of Services is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Services tab.  ---   ### Detail APIs  The Detail APIs are read-only APIs used to list all the Infrastructure resources (Hosts and Services). Each resource record returned also contains information about its other associated resources and the status information for itself and the associated resource(s) (i.e., Host/Service status).  ---   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infra_mgmt.models.detail_host_service_config import DetailHostServiceConfig
from infra_mgmt.models.detail_location import DetailLocation
from infra_mgmt.models.pool_info import PoolInfo
from typing import Optional, Set
from typing_extensions import Self


class DetailHost(BaseModel):
    """
    DetailHost
    """

  # noqa: E501
    composite_status: Optional[StrictStr] = Field(
        default=None,
        description=
        "Composite Status of this Host (`online`, `degraded`, `error`, `offline`, `pending`, `awaiting approval`)."
    )
    configs: Optional[List[DetailHostServiceConfig]] = Field(
        default=None,
        description=
        "The list of Host-specific configurations for each Service deployed on this Host."
    )
    connectivity_monitor: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = Field(
        default=None, description="The timestamp of creation of Host.")
    description: Optional[StrictStr] = Field(
        default=None, description="The description of the Host.")
    display_name: Optional[StrictStr] = Field(
        default=None, description="The name of the Host.")
    host_subtype: Optional[StrictStr] = Field(
        default=None,
        description=
        "The sub-type of a specific Host type.  Example: For Host type BloxOne Appliance, sub-type could be \"B105\" or \"VEP1425\""
    )
    host_type: Optional[StrictStr] = None
    host_version: Optional[StrictStr] = Field(
        default=None, description="The version of the Host platform services.")
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    ip_address: Optional[StrictStr] = Field(
        default=None, description="The IP address of the Host.")
    ip_space: Optional[StrictStr] = Field(
        default=None, description="The IP Space of the Host.")
    legacy_id: Optional[StrictStr] = Field(
        default=None, description="The legacy Host object identifier.")
    location: Optional[DetailLocation] = Field(
        default=None,
        description="Location that this Host is associated with.")
    mac_address: Optional[StrictStr] = Field(
        default=None, description="The MAC address of the Host.")
    maintenance_mode: Optional[StrictStr] = None
    nat_ip: Optional[StrictStr] = Field(
        default=None, description="The NAT IP address of the Host.")
    ophid: Optional[StrictStr] = Field(
        default=None,
        description=
        "The unique On-Prem Host ID generated by the On-Prem device and assigned to the Host once it is registered and logged into the Infoblox Cloud."
    )
    pool: Optional[PoolInfo] = Field(
        default=None, description="Pool information for this Host (internal).")
    serial_number: Optional[StrictStr] = Field(
        default=None, description="The unique serial number of the Host.")
    services: Optional[List[DetailHostServiceConfig]] = Field(
        default=None,
        description="The list of Services deployed on this Host.")
    site_id: Optional[StrictStr] = Field(
        default=None, description="The Site ID of the Host.")
    tags: Optional[Dict[str, Any]] = Field(
        default=None, description="Tags associated with this Host.")
    timezone: Optional[StrictStr] = Field(
        default=None, description="The timezone of the Host.")
    updated_at: Optional[datetime] = Field(
        default=None,
        description="The timestamp of the latest update on Host.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "composite_status", "configs", "connectivity_monitor", "created_at",
        "description", "display_name", "host_subtype", "host_type",
        "host_version", "id", "ip_address", "ip_space", "legacy_id",
        "location", "mac_address", "maintenance_mode", "nat_ip", "ophid",
        "pool", "serial_number", "services", "site_id", "tags", "timezone",
        "updated_at"
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
        """Create an instance of DetailHost from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in configs (list)
        _items = []
        if self.configs:
            for _item in self.configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['configs'] = _items
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pool
        if self.pool:
            _dict['pool'] = self.pool.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in services (list)
        _items = []
        if self.services:
            for _item in self.services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['services'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DetailHost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "composite_status":
            obj.get("composite_status"),
            "configs": [
                DetailHostServiceConfig.from_dict(_item)
                for _item in obj["configs"]
            ] if obj.get("configs") is not None else None,
            "connectivity_monitor":
            obj.get("connectivity_monitor"),
            "created_at":
            obj.get("created_at"),
            "description":
            obj.get("description"),
            "display_name":
            obj.get("display_name"),
            "host_subtype":
            obj.get("host_subtype"),
            "host_type":
            obj.get("host_type"),
            "host_version":
            obj.get("host_version"),
            "id":
            obj.get("id"),
            "ip_address":
            obj.get("ip_address"),
            "ip_space":
            obj.get("ip_space"),
            "legacy_id":
            obj.get("legacy_id"),
            "location":
            DetailLocation.from_dict(obj["location"])
            if obj.get("location") is not None else None,
            "mac_address":
            obj.get("mac_address"),
            "maintenance_mode":
            obj.get("maintenance_mode"),
            "nat_ip":
            obj.get("nat_ip"),
            "ophid":
            obj.get("ophid"),
            "pool":
            PoolInfo.from_dict(obj["pool"])
            if obj.get("pool") is not None else None,
            "serial_number":
            obj.get("serial_number"),
            "services": [
                DetailHostServiceConfig.from_dict(_item)
                for _item in obj["services"]
            ] if obj.get("services") is not None else None,
            "site_id":
            obj.get("site_id"),
            "tags":
            obj.get("tags"),
            "timezone":
            obj.get("timezone"),
            "updated_at":
            obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
