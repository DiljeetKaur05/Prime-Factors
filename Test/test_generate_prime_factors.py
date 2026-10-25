"""Test cases for the prime factors function."""

import pytest
from prime import generate_prime_factors


def test_invalid_input():
    """Check that invalid inputs raise a ValueError."""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")

    with pytest.raises(ValueError):
        generate_prime_factors(2.5)


def test_input_one():
    """Check that 1 returns an empty list."""
    result = generate_prime_factors(1)
    assert isinstance(result, list)
    assert not result


def test_input_two():
    """Check that 2 returns [2]."""
    assert generate_prime_factors(2) == [2]


def test_input_three():
    """Check that 3 returns [3]."""
    assert generate_prime_factors(3) == [3]


def test_input_four():
    """Check that 4 returns [2, 2]."""
    assert generate_prime_factors(4) == [2, 2]


def test_input_six():
    """Check that 6 returns [2, 3]."""
    assert generate_prime_factors(6) == [2, 3]


def test_input_eight():
    """Check that 8 returns [2, 2, 2]."""
    assert generate_prime_factors(8) == [2, 2, 2]


def test_input_nine():
    """Check that 9 returns [3, 3]."""
    assert generate_prime_factors(9) == [3, 3]
