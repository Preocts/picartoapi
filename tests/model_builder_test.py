"""Test all models against fixture responses"""
import json
from pathlib import Path

import pytest
from picartoapi.model.base_model import BaseModel
from picartoapi.model.category import Category
from picartoapi.model.channel import Channel
from picartoapi.model.channel_stub import ChannelStub


@pytest.mark.parametrize(
    ("fixture_path", "object_ref"),
    (
        ("tests/resp/categories.json", Category),
        ("tests/resp/channels.json", ChannelStub),
        ("tests/resp/channel.json", Channel),
    ),
)
def test_all_models(fixture_path: str, object_ref: BaseModel) -> None:
    fixture = json.load(Path(fixture_path).open())

    models = [object_ref.build_from(obj) for obj in fixture]

    # Validate model contents against resp json
    for obj, model in zip(fixture, models):
        model_json = json.dumps(model.to_json(), sort_keys=True)
        fixture_json = json.dumps(obj, sort_keys=True)

        assert model_json == fixture_json
