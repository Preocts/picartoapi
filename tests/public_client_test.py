from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import patch

import httpx
import pytest
from picartoapi.public_client import PublicClient

CATAGORIES_RESP = Path("tests/resp/categories.json").read_text()
ONLINE_RESP = Path("tests/resp/online.json").read_text()
CHANNEL_RESP = Path("tests/resp/channel.json").read_text()
VIDEO_RESP = Path("tests/resp/videos.json").read_text()
CHANNELS_RESP = Path("tests/resp/channels.json").read_text()
VIDEO_SEARCH_RESP = Path("tests/resp/searchvideo.json").read_text()


@pytest.mark.parametrize(
    ("attrib", "route", "resp", "kwargs", "expected"),
    (
        ("categories", "/categories", CATAGORIES_RESP, {}, True),
        ("categories", "/categories", "", {}, False),
        ("online", "/online", ONLINE_RESP, {}, True),
        ("online", "/online", "", {}, False),
        ("channel", "/channel/name/test", CHANNEL_RESP, {"channel": "test"}, True),
        ("channel", "/channel/name/test", "", {"channel": "test"}, False),
        ("channel", "/channel/id/123", CHANNEL_RESP, {"channel": 123}, True),
        ("channel", "/channel/id/123", "", {"channel": 123}, False),
        ("videos", "/channel/name/test/videos", VIDEO_RESP, {"channel": "test"}, True),
        ("videos", "/channel/name/test/videos", "", {"channel": "test"}, False),
        ("videos", "/channel/id/123/videos", VIDEO_RESP, {"channel": 123}, True),
        ("videos", "/channel/id/123/videos", "", {"channel": 123}, False),
        ("search_channels", "/search/channels", CHANNELS_RESP, {"query": "test"}, True),
        ("search_channels", "/search/channels", "", {"query": "test"}, False),
        ("search_videos", "/search/videos", VIDEO_SEARCH_RESP, {"query": "test"}, True),
        ("search_videos", "/search/videos", "", {"query": "test"}, False),
    ),
)
def test_get_method_resp_handling(
    attrib: str,
    route: str,
    resp: str,
    kwargs: dict[str, Any],
    expected: bool,
) -> None:
    mock_resp = httpx.Response(status_code=200 if resp else 404, content=resp.encode())
    client = PublicClient()
    with patch.object(client._http, "get", return_value=mock_resp):

        results = getattr(client, attrib)(**kwargs)

    assert bool(results) == expected
