from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class ChatSettings(BaseModel):
    """Define an empty ChatSetting obejct."""

    guest_chat: bool
    links: bool
    level: bool

    @classmethod
    def build_from(cls, settings: dict[str, Any]) -> ChatSettings:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.guest_chat = settings.get("guest_chat") or False
        new_obj.links = settings.get("links") or False
        new_obj.level = settings.get("level") or False
        return new_obj
