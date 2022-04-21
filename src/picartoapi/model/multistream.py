from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class Multistream(BaseModel):
    """Define an empty Multistream obejct."""

    user_id: int
    name: str
    online: bool
    adult: bool

    @classmethod
    def build_from(cls, channel: dict[str, Any]) -> Multistream:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.user_id = channel.get("user_id") or 0
        new_obj.name = channel.get("name") or ""
        new_obj.online = channel.get("online") or False
        new_obj.adult = channel.get("adult") or False
        return new_obj
