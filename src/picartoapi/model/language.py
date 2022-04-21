from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel


class Language(BaseModel):
    """Define an empty Language obejct."""

    id: int  # noqa A003 - Following API naming
    name: str

    @classmethod
    def build_from(cls, language: dict[str, Any]) -> Language:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.id = language.get("id") or 0
        new_obj.name = language.get("name") or ""
        return new_obj
