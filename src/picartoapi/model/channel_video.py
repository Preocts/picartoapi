from __future__ import annotations

from typing import Any

from picartoapi.model.base_model import BaseModel
from picartoapi.model.channel_stub import ChannelStub
from picartoapi.model.video import Video


class ChannelVideo(BaseModel):
    """Define an empty ChannelVideo obejct."""

    channel: ChannelStub
    video: Video

    @classmethod
    def build_from(cls, channelvideo: dict[str, Any]) -> ChannelVideo:
        """Build object from HTTP response."""
        new_obj = cls()
        new_obj.channel = ChannelStub.build_from(channelvideo.get("channel") or {})
        new_obj.video = Video.build_from(channelvideo.get("video") or {})
        return new_obj
