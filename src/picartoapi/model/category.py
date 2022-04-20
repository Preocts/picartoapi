from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class Category(BaseModel):
    """Define an empty Catagory obejct."""

    id: int  # noqa: A003  mirroring API model
    name: str
    adult: bool
    is_active: bool
    image: str
    created_at: str
    updated_at: str
    deleted_at: str | None
    total_viewers: int
    total_channels: int
    online_channels: int
    total_views: int

    @classmethod
    def build_from(cls, catagory: dict[str, Any]) -> Category:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.id = catagory.get("id") or 0
        new_obj.name = catagory.get("name") or ""
        new_obj.adult = catagory.get("adult") or False
        new_obj.is_active = catagory.get("is_active") or False
        new_obj.image = catagory.get("image") or ""
        new_obj.created_at = catagory.get("created_at") or ""
        new_obj.updated_at = catagory.get("updated_at") or ""
        new_obj.deleted_at = catagory.get("deleted_at")
        new_obj.total_viewers = catagory.get("total_viewers") or 0
        new_obj.total_channels = catagory.get("total_channels") or 0
        new_obj.online_channels = catagory.get("online_channels") or 0
        new_obj.total_views = catagory.get("total_views") or 0
        return new_obj
