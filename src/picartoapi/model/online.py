from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel
from picartoapi.model.language import Language
from picartoapi.model.thumbnails import Thumbnails


class Online(BaseModel):
    """Define an empty Online obejct."""

    user_id: int
    name: str
    avatar: str
    title: str
    viewers: int
    thumbnails: Thumbnails
    category: list[str]
    account_type: str
    adult: bool
    gaming: bool
    commissions: bool
    multistream: bool
    languages: list[Language]
    following: bool

    @classmethod
    def build_from(cls, channel: dict[str, Any]) -> Online:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.user_id = channel.get("user_id") or 0
        new_obj.name = channel.get("name") or ""
        new_obj.avatar = channel.get("avatar") or ""
        new_obj.title = channel.get("title") or ""
        new_obj.viewers = channel.get("viewers") or 0
        new_obj.thumbnails = Thumbnails.build_from(channel.get("thumbnails") or {})
        new_obj.category = channel.get("category") or []
        new_obj.account_type = channel.get("account_type") or ""
        new_obj.adult = channel.get("adult") or False
        new_obj.gaming = channel.get("gaming") or False
        new_obj.commissions = channel.get("commissions") or False
        new_obj.multistream = channel.get("multistream") or False
        languages = channel.get("languages") or []
        new_obj.languages = [Language.build_from(lang) for lang in languages]
        new_obj.following = channel.get("following") or False
        return new_obj
