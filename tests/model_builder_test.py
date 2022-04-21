"""Test all models against fixture responses"""
import json
from pathlib import Path

import pytest
from picartoapi.model.base_model import BaseModel
from picartoapi.model.category import Category
from picartoapi.model.channel_stub import ChannelStub


@pytest.mark.parametrize(
    ("fixture_path", "object_ref"),
    (
        ("tests/resp/categories.json", Category),
        ("tests/resp/channels.json", ChannelStub),
    ),
)
def test_all_models(fixture_path: str, object_ref: BaseModel) -> None:
    fixture = json.load(Path(fixture_path).open())

    models = [object_ref.build_from(obj) for obj in fixture]

    # Validate model contents against resp json
    for obj, model in zip(fixture, models):
        assert model.to_json() == obj
        for key, value in obj.items():
            assert getattr(model, key) == value
