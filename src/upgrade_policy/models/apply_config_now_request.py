# coding: utf-8

"""
    Schedule Software/Config Updates

    Infoblox by default does automatic software updates when they become available. Updates are applied to all on-prem hosts, physical or virtual. However, you can override and schedule the software updates. You can also defer the updates to a later date and time. You can configure up to a total of 50 deferrals (scheduled and deferred software updates), which means you have the flexibility to create up to 50 update groups across different on-prem hosts by mapping with appropriate tags. Tags are be used to associate deferrals (scheduled or deferred) with a specific or group of onprem-hosts. Apart from software update deferrals, config update deferrals also can be configured using these overrides.

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from upgrade_policy.models.onprem_details import OnpremDetails
from typing import Optional, Set
from typing_extensions import Self


class ApplyConfigNowRequest(BaseModel):
    """
    ApplyConfigNowRequest
    """

  # noqa: E501
    payload: Optional[List[OnpremDetails]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["payload"]

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
        """Create an instance of ApplyConfigNowRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in payload (list)
        _items = []
        if self.payload:
            for _item in self.payload:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payload'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplyConfigNowRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payload":
            [OnpremDetails.from_dict(_item) for _item in obj["payload"]]
            if obj.get("payload") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
