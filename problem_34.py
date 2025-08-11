from operator import mul
from functools import reduce


def factorial(n: int) -> int:
    return reduce(mul, range(1, n + 1), 1)


def get_digit_factorial(n: str) -> int:
    total = 0
    for c in n:
        total += factorial(int(c))
    return total


def is_equal_fac_digit(n: int) -> bool:
    return n == get_digit_factorial(str(n))


def get_numbers(n):
    for i in range(3, n + 1):
        if is_equal_fac_digit(i):
            yield i


print(sum(get_numbers(10**5)))
