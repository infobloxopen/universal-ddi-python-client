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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ipam.models.inheritance_inherited_bool import InheritanceInheritedBool
from ipam.models.inheritance_inherited_float import InheritanceInheritedFloat
from ipam.models.inheritance_inherited_identifier import InheritanceInheritedIdentifier
from ipam.models.inheritance_inherited_string import InheritanceInheritedString
from ipam.models.inherited_ddns_block import InheritedDDNSBlock
from ipam.models.inherited_ddns_hostname_block import InheritedDDNSHostnameBlock
from ipam.models.inherited_dhcp_config import InheritedDHCPConfig
from ipam.models.inherited_dhcp_option_list import InheritedDHCPOptionList
from ipam.models.inherited_hostname_rewrite_block import InheritedHostnameRewriteBlock
from typing import Optional, Set
from typing_extensions import Self


class ServerInheritance(BaseModel):
    """
    The inheritance configuration specifies how and which fields _Server_ object (DHCP Config Profile) inherits from _Global_ parent.
    """ # noqa: E501
    ddns_block: Optional[InheritedDDNSBlock] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_enabled_, _ddns_send_updates_, _ddns_domain_, _ddns_zones_ fields from _Server_ object."
    )
    ddns_client_update: Optional[InheritanceInheritedString] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_client_update_ field from _Server_ object."
    )
    ddns_conflict_resolution_mode: Optional[InheritanceInheritedString] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_conflict_resolution_mode_ field from _Server_ object."
    )
    ddns_hostname_block: Optional[InheritedDDNSHostnameBlock] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_generate_name_ and _ddns_generated_prefix_ fields from _Server_ object."
    )
    ddns_ttl_percent: Optional[InheritanceInheritedFloat] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_ttl_percent_ field from _Server_ object."
    )
    ddns_update_on_renew: Optional[InheritanceInheritedBool] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_update_on_renew_ field from _Server_ object."
    )
    ddns_use_conflict_resolution: Optional[InheritanceInheritedBool] = Field(
        default=None,
        description=
        "The inheritance configuration for _ddns_use_conflict_resolution_ field from _Server_ object."
    )
    dhcp_config: Optional[InheritedDHCPConfig] = Field(
        default=None,
        description=
        "The inheritance configuration for _dhcp_config_ field from _Server_ object."
    )
    dhcp_options: Optional[InheritedDHCPOptionList] = Field(
        default=None,
        description=
        "The inheritance configuration for _dhcp_options_ field from _Server_ object."
    )
    dhcp_options_v6: Optional[InheritedDHCPOptionList] = Field(
        default=None,
        description=
        "The inheritance configuration for _dhcp_options_v6_ field from _Server_ object."
    )
    header_option_filename: Optional[InheritanceInheritedString] = Field(
        default=None,
        description=
        "The inheritance configuration for _header_option_filename_ field.")
    header_option_server_address: Optional[InheritanceInheritedString] = Field(
        default=None,
        description=
        "The inheritance configuration for _header_option_server_address_ field."
    )
    header_option_server_name: Optional[InheritanceInheritedString] = Field(
        default=None,
        description=
        "The inheritance configuration for _header_option_server_name_ field.")
    hostname_rewrite_block: Optional[InheritedHostnameRewriteBlock] = Field(
        default=None,
        description=
        "The inheritance configuration for _hostname_rewrite_enabled_, _hostname_rewrite_regex_, _hostname_rewrite_char_ fields from _Server_ object."
    )
    vendor_specific_option_option_space: Optional[
        InheritanceInheritedIdentifier] = Field(
            default=None,
            description=
            "The inheritance configuration for _vendor_specific_option_option_space_ field from _Server_ object."
        )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "ddns_block", "ddns_client_update", "ddns_conflict_resolution_mode",
        "ddns_hostname_block", "ddns_ttl_percent", "ddns_update_on_renew",
        "ddns_use_conflict_resolution", "dhcp_config", "dhcp_options",
        "dhcp_options_v6", "header_option_filename",
        "header_option_server_address", "header_option_server_name",
        "hostname_rewrite_block", "vendor_specific_option_option_space"
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
        """Create an instance of ServerInheritance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ddns_block
        if self.ddns_block:
            _dict['ddns_block'] = self.ddns_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ddns_client_update
        if self.ddns_client_update:
            _dict['ddns_client_update'] = self.ddns_client_update.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ddns_conflict_resolution_mode
        if self.ddns_conflict_resolution_mode:
            _dict[
                'ddns_conflict_resolution_mode'] = self.ddns_conflict_resolution_mode.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of ddns_hostname_block
        if self.ddns_hostname_block:
            _dict['ddns_hostname_block'] = self.ddns_hostname_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ddns_ttl_percent
        if self.ddns_ttl_percent:
            _dict['ddns_ttl_percent'] = self.ddns_ttl_percent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ddns_update_on_renew
        if self.ddns_update_on_renew:
            _dict['ddns_update_on_renew'] = self.ddns_update_on_renew.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ddns_use_conflict_resolution
        if self.ddns_use_conflict_resolution:
            _dict[
                'ddns_use_conflict_resolution'] = self.ddns_use_conflict_resolution.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of dhcp_config
        if self.dhcp_config:
            _dict['dhcp_config'] = self.dhcp_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dhcp_options
        if self.dhcp_options:
            _dict['dhcp_options'] = self.dhcp_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dhcp_options_v6
        if self.dhcp_options_v6:
            _dict['dhcp_options_v6'] = self.dhcp_options_v6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of header_option_filename
        if self.header_option_filename:
            _dict[
                'header_option_filename'] = self.header_option_filename.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of header_option_server_address
        if self.header_option_server_address:
            _dict[
                'header_option_server_address'] = self.header_option_server_address.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of header_option_server_name
        if self.header_option_server_name:
            _dict[
                'header_option_server_name'] = self.header_option_server_name.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of hostname_rewrite_block
        if self.hostname_rewrite_block:
            _dict[
                'hostname_rewrite_block'] = self.hostname_rewrite_block.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of vendor_specific_option_option_space
        if self.vendor_specific_option_option_space:
            _dict[
                'vendor_specific_option_option_space'] = self.vendor_specific_option_option_space.to_dict(
                )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServerInheritance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ddns_block":
            InheritedDDNSBlock.from_dict(obj["ddns_block"])
            if obj.get("ddns_block") is not None else None,
            "ddns_client_update":
            InheritanceInheritedString.from_dict(obj["ddns_client_update"])
            if obj.get("ddns_client_update") is not None else None,
            "ddns_conflict_resolution_mode":
            InheritanceInheritedString.from_dict(
                obj["ddns_conflict_resolution_mode"])
            if obj.get("ddns_conflict_resolution_mode") is not None else None,
            "ddns_hostname_block":
            InheritedDDNSHostnameBlock.from_dict(obj["ddns_hostname_block"])
            if obj.get("ddns_hostname_block") is not None else None,
            "ddns_ttl_percent":
            InheritanceInheritedFloat.from_dict(obj["ddns_ttl_percent"])
            if obj.get("ddns_ttl_percent") is not None else None,
            "ddns_update_on_renew":
            InheritanceInheritedBool.from_dict(obj["ddns_update_on_renew"])
            if obj.get("ddns_update_on_renew") is not None else None,
            "ddns_use_conflict_resolution":
            InheritanceInheritedBool.from_dict(
                obj["ddns_use_conflict_resolution"])
            if obj.get("ddns_use_conflict_resolution") is not None else None,
            "dhcp_config":
            InheritedDHCPConfig.from_dict(obj["dhcp_config"])
            if obj.get("dhcp_config") is not None else None,
            "dhcp_options":
            InheritedDHCPOptionList.from_dict(obj["dhcp_options"])
            if obj.get("dhcp_options") is not None else None,
            "dhcp_options_v6":
            InheritedDHCPOptionList.from_dict(obj["dhcp_options_v6"])
            if obj.get("dhcp_options_v6") is not None else None,
            "header_option_filename":
            InheritanceInheritedString.from_dict(obj["header_option_filename"])
            if obj.get("header_option_filename") is not None else None,
            "header_option_server_address":
            InheritanceInheritedString.from_dict(
                obj["header_option_server_address"])
            if obj.get("header_option_server_address") is not None else None,
            "header_option_server_name":
            InheritanceInheritedString.from_dict(
                obj["header_option_server_name"])
            if obj.get("header_option_server_name") is not None else None,
            "hostname_rewrite_block":
            InheritedHostnameRewriteBlock.from_dict(
                obj["hostname_rewrite_block"])
            if obj.get("hostname_rewrite_block") is not None else None,
            "vendor_specific_option_option_space":
            InheritanceInheritedIdentifier.from_dict(
                obj["vendor_specific_option_option_space"])
            if obj.get("vendor_specific_option_option_space") is not None else
            None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
