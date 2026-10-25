import pytest
from prime import generate_prime_factors


def test_invalid_input():
    with pytest.raises(ValueError):
        generate_prime_factors("hello")

    with pytest.raises(ValueError):
        generate_prime_factors(2.5)


def test_input_one():
    assert generate_prime_factors(1) == []

def test_input_two():
    assert generate_prime_factors(2) == [2]

def test_input_three():
    assert generate_prime_factors(3) == [3]


def test_input_four():
    assert generate_prime_factors(4) == [2, 2]


def test_input_six():
    assert generate_prime_factors(6) == [2, 3]