# d(n) = sum of all divisors of n
# d(a) = b, d(b) = a, where a != b

from functools import cache

MAX_NUMBER = 10 ** 4
amicables_sum = 0


@cache
def d(n: int) -> int:
    divisors_sum = 0
    max_range = None
    if is_even(n):
        max_range = int((n / 2) + 1)
    else:
        max_range = int((n - 1) / 2 + 1)
    for i in range(1, max_range):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_amicable(n: int) -> bool:
    amicable = d(n)
    if amicable == n:
        return False
    return d(amicable) == n


for n in range(2, MAX_NUMBER):
    if is_amicable(n):
        amicables_sum += n

print(amicables_sum)
