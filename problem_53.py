from functools import cache


@cache
def factorial(n: int) -> int:
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def calc_comb(n: int, r: int) -> int:
    return factorial(n) / (factorial(n - r) * factorial(r))


GREATER_THAN = 10 ** 6
total = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        if calc_comb(n, r) > GREATER_THAN:
            total += 1

print(total)