from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class ChannelStub(BaseModel):
    """Define an empty Channel obejct."""

    user_id: int
    name: str
    avatar: str
    online: bool

    @classmethod
    def build_from(cls, channel: dict[str, Any]) -> ChannelStub:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.user_id = channel.get("user_id") or 0
        new_obj.name = channel.get("name") or ""
        new_obj.avatar = channel.get("avatar") or ""
        new_obj.online = channel.get("online") or False
        return new_obj
