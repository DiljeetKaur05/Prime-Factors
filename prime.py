def generate_prime_factors(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    factors = []

    while number > 1 and number % 2 == 0:
        factors.append(2)
        number = number // 2

    if number > 1:
        factors.append(number)

    return factors