from src.cart_total import calculate_total
import pytest

#sad path (for type error)
@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        (1.5, 1),
        ("100", 1),
        (True, 1),
        (0, 1.5),
        (1, "4"),
        (250, False),
    ],
)

def test_cart_total_with_invalid_type_raises_error(unit_price_cents,quantity):

    with pytest.raises(TypeError):
        calculate_total(unit_price_cents, quantity)

#sad path (for out of range value error)
@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        (-1, 1),
        (250, -1),
    ],
)

def test_cart_total_with_out_of_range_inputs_raises_error(unit_price_cents,quantity):

    with pytest.raises(ValueError):
        calculate_total(unit_price_cents, quantity)


#Happy path
@pytest.mark.parametrize(
    "unit_price_cents, quantity, expected",
    [
        (250, 4, 1000),
        (0, 1, 0),
        (1, 0, 0),
    ],
)

def test_cart_total_with_valid_inputs_returns_total(unit_price_cents, quantity, expected):
    assert calculate_total(unit_price_cents, quantity) == expected



