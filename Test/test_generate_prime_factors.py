import pytest
from prime import generate_prime_factors


def test_invalid_input():
    with pytest.raises(ValueError):
        generate_prime_factors("hello")

    with pytest.raises(ValueError):
        generate_prime_factors(2.5)


def test_input_one():
    assert generate_prime_factors(1) == []