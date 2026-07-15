import random

import pytest

from src.generator import generate_items


def test_generate_items_returns_requested_count():
    items = generate_items(10, rng=random.Random(42))
    assert len(items) == 10


def test_generate_items_have_valid_fields():
    items = generate_items(5, rng=random.Random(1))
    for name, quantity in items:
        assert isinstance(name, str) and name
        assert isinstance(quantity, int)
        assert 1 <= quantity <= 500


def test_generate_items_is_reproducible_with_same_seed():
    a = generate_items(20, rng=random.Random(7))
    b = generate_items(20, rng=random.Random(7))
    assert a == b


def test_generate_items_zero_count_returns_empty_list():
    assert generate_items(0) == []


def test_generate_items_negative_count_raises_value_error():
    with pytest.raises(ValueError):
        generate_items(-1)
