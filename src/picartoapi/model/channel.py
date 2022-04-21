from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel
from picartoapi.model.chat_settings import ChatSettings
from picartoapi.model.description_panel import DescriptionPanel
from picartoapi.model.language import Language
from picartoapi.model.multistream import Multistream
from picartoapi.model.thumbnails import Thumbnails


class Channel(BaseModel):
    """Define an empty Channel obejct."""

    user_id: int
    name: str
    avatar: str
    online: bool
    viewers: int
    viewers_total: int
    thumbnails: Thumbnails
    followers: int
    subscribers: int
    adult: bool
    category: list[str]
    account_type: str
    commissions: bool
    recordings: bool
    title: str
    description_panels: list[DescriptionPanel]
    private: bool
    private_message: str
    gaming: bool
    chat_settings: ChatSettings
    last_live: str
    tags: list[str]
    multistream: list[Multistream]
    languages: list[Language]
    following: bool
    creation_date: str

    @classmethod
    def build_from(cls, channel: dict[str, Any]) -> Channel:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.user_id = channel.get("user_id") or 0
        new_obj.name = channel.get("name") or ""
        new_obj.avatar = channel.get("avatar") or ""
        new_obj.online = channel.get("online") or False
        new_obj.viewers = channel.get("viewers") or 0
        new_obj.viewers_total = channel.get("viewers_total") or 0
        new_obj.thumbnails = Thumbnails.build_from(channel.get("thumbnails") or {})
        new_obj.followers = channel.get("followers") or 0
        new_obj.subscribers = channel.get("subscribers") or 0
        new_obj.adult = channel.get("adult") or False
        new_obj.category = channel.get("category") or []
        new_obj.account_type = channel.get("account_type") or ""
        new_obj.commissions = channel.get("commissions") or False
        new_obj.recordings = channel.get("recordings") or False
        new_obj.title = channel.get("title") or ""
        panels = channel.get("description_panels") or []
        new_obj.description_panels = [DescriptionPanel.build_from(p) for p in panels]
        new_obj.private = channel.get("private") or False
        new_obj.private_message = channel.get("private_message") or ""
        new_obj.gaming = channel.get("gaming") or False
        settings = channel.get("chat_settings") or {}
        new_obj.chat_settings = ChatSettings.build_from(settings)
        new_obj.last_live = channel.get("last_live") or ""
        new_obj.tags = channel.get("tags") or []
        mstreams = channel.get("multistream") or []
        new_obj.multistream = [Multistream.build_from(ms) for ms in mstreams]
        languages = channel.get("languages") or []
        new_obj.languages = [Language.build_from(lang) for lang in languages]
        new_obj.following = channel.get("following") or False
        new_obj.creation_date = channel.get("creation_date") or ""
        return new_obj
