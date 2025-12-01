import math

import pytest

from sample_app import calculator


def test_add_handles_varargs():
    assert calculator.add(1, 2, 3.5) == pytest.approx(6.5)


def test_multiply_accepts_ints_and_floats():
    assert calculator.multiply(3, 0.5) == pytest.approx(1.5)


def test_average_rejects_empty_iterable():
    with pytest.raises(ValueError):
        calculator.average([])


def test_average_matches_math_mean():
    values = [2, 4, 6, 8]
    assert calculator.average(values) == pytest.approx(sum(values) / len(values))


def test_average_handles_tuple_input():
    values = (1, 2, 3)
    assert calculator.average(values) == pytest.approx(math.fsum(values) / len(values))
