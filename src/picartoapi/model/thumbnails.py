from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class Thumbnails(BaseModel):
    """Define an empty Thumbnails obejct."""

    web: str
    web_large: str
    mobile: str
    tablet: str

    @classmethod
    def build_from(cls, thumbnails: dict[str, Any]) -> Thumbnails:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.web = thumbnails.get("web") or ""
        new_obj.web_large = thumbnails.get("web_large") or ""
        new_obj.mobile = thumbnails.get("mobile") or ""
        new_obj.tablet = thumbnails.get("tablet") or ""
        return new_obj
