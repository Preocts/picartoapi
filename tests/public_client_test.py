import json
from pathlib import Path
from typing import Generator
from unittest.mock import patch

import pytest
from http_overeasy.client_mocker import ClientMocker as HTTPMocker
from picartoapi.public_client import PublicClient

MOCK_RESP = json.load(Path("tests/resp/categories.json").open())


@pytest.fixture
def client() -> Generator[PublicClient, None, None]:
    client = PublicClient()
    mocker = HTTPMocker()
    with patch.object(client, "http", mocker):
        yield client


def test_catagories_success(client: PublicClient) -> None:
    url = f"{client.base_url}/categories"
    client.http.add_response(
        response_body=MOCK_RESP,
        response_headers={},
        status=200,
        url=url,
    )

    results = client.catagories()

    assert isinstance(results, list)
    assert results


def test_catagories_failure(client: PublicClient) -> None:
    url = f"{client.base_url}/categories"
    client.http.add_response(
        response_body={},
        response_headers={},
        status=404,
        url=url,
    )

    results = client.catagories()

    assert not results
