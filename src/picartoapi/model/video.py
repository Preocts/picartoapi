from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel
from picartoapi.model.thumbnails import Thumbnails


class Video(BaseModel):
    """Define an empty Video obejct."""

    id: int  # noqa A003
    title: str
    stream_name: str
    thumbnails: Thumbnails
    file: str  # noqa A003
    filesize: int
    duration: int
    views: int
    timestamp: str
    adult: bool

    @classmethod
    def build_from(cls, video: dict[str, Any]) -> Video:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.id = video.get("id") or 0
        new_obj.title = video.get("title") or ""
        new_obj.stream_name = video.get("stream_name") or ""

        # This attribute is excluded in the return of video searches
        # Easier to delete here than build another model
        if not new_obj.stream_name:
            delattr(new_obj, "stream_name")

        new_obj.thumbnails = Thumbnails.build_from(video.get("thumbnails") or {})
        new_obj.file = video.get("file") or ""
        new_obj.filesize = video.get("filesize") or 0
        new_obj.duration = video.get("duration") or 0
        new_obj.views = video.get("views") or 0
        new_obj.timestamp = video.get("timestamp") or ""
        new_obj.adult = video.get("adult") or False
        return new_obj
