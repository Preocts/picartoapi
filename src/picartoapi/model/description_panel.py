from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class DescriptionPanel(BaseModel):
    """Define an empty DescriptionPanel obejct."""

    title: str
    body: str
    image: str
    image_link: str
    button_text: str
    button_link: str
    position: int

    @classmethod
    def build_from(cls, panel: dict[str, Any]) -> DescriptionPanel:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.title = panel.get("title") or ""
        new_obj.body = panel.get("body") or ""
        new_obj.image = panel.get("image") or ""
        new_obj.image_link = panel.get("image_link") or ""
        new_obj.button_text = panel.get("button_text") or ""
        new_obj.button_link = panel.get("button_link") or ""
        new_obj.position = panel.get("position") or 0
        return new_obj
