import pytest
from func import get_period

period_parameters = [
    (0, "ночь"),
    (6, "ночь"),
    (7, "утро"),
    (11, "утро"),
    (12, "день"),
    (17, "день"),
    (18, "вечер"),
    (24, "вечер")
]


@pytest.mark.parametrize("period_int, period_str", period_parameters)
def test_get_period(period_int, period_str):
    assert get_period(period_int) == period_str


period_exception = [
    (-1, ValueError),
    (25, ValueError),
    ("5", TypeError),
    (5.0, TypeError)
]


@pytest.mark.parametrize("period_int, exception", period_exception)
def test_get_period_exception(period_int, exception):
    with pytest.raises(exception):
        assert get_period(period_int) == exception

