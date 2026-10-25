def generate_prime_factors(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    factors = []
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    if number > 1:
        factors.append(number)

    return factors