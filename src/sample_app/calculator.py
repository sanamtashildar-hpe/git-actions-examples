from __future__ import annotations


def add(*values: float) -> float:
    """Add any number of numeric values and return the sum."""
    total = 0.0
    for value in values:
        total += float(value)
    return total


def multiply(a: float, b: float) -> float:
    """Return the product of two numeric values."""
    return float(a) * float(b)


def average(values: list[float] | tuple[float, ...]) -> float:
    """Return the arithmetic mean, raising ValueError for empty inputs."""
    if not values:
        raise ValueError("average() requires at least one value")
    return sum(values) / len(values)
