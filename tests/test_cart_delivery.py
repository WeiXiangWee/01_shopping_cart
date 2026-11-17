from src.cart_delivery import qualifies_free_delivery
import pytest

#sad path (for type error)
@pytest.mark.parametrize(
    "total_cents",
    [
        (5000.1),
        ("5000"),
        (True),

    ],
)

def test_cart_delivery_with_invalid_type_raises_error(total_cents):

    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)

#sad path (for out of range value error)

def test_cart_delivery_with_out_of_range_inputs_raises_error():
    total_cents = -1

    with pytest.raises(ValueError):
        qualifies_free_delivery(total_cents)


#Happy path
@pytest.mark.parametrize(
    "total_cents, expected",
    [
        (0, False),
        (4999, False),
        (5000, True),
        (5001, True)
    ],
)

def test_cart_total_with_valid_inputs_returns_true(total_cents, expected):
    assert qualifies_free_delivery(total_cents) == expected



