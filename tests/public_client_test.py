from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from typing import Generator
from unittest.mock import patch

import pytest
from http_overeasy.client_mocker import ClientMocker as HTTPMocker
from picartoapi.public_client import PublicClient

CATAGORIES_RESP = json.load(Path("tests/resp/categories.json").open())
ONLINE_RESP = json.load(Path("tests/resp/online.json").open())
CHANNEL_RESP = json.load(Path("tests/resp/channel.json").open())


@pytest.fixture
def client() -> Generator[PublicClient, None, None]:
    client = PublicClient()
    mocker = HTTPMocker()
    with patch.object(client, "http", mocker):
        yield client


@pytest.mark.parametrize(
    ("method", "route", "resp", "kwargs", "expected"),
    (
        ("categories", "/categories", CATAGORIES_RESP, {}, True),
        ("categories", "/categories", {}, {}, False),
        ("online", "/online", ONLINE_RESP, {}, True),
        ("online", "/online", {}, {}, False),
    ),
)
def test_method_resp_handling(
    client: PublicClient,
    method: str,
    route: str,
    resp: dict[str, Any],
    kwargs: dict[str, Any],
    expected: bool,
) -> None:
    client.http.add_response(
        response_body=resp,
        response_headers={},
        status=200 if resp else 404,
        url=f"{client.base_url}{route}",
    )

    results = getattr(client, method)(**kwargs)

    assert isinstance(results, list)
    assert bool(results) == expected
