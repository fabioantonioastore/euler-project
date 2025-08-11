from typing import Generator


def get_pow_and_get_digit_sum() -> Generator:
    for a in range(1, 100):
        for b in range(1, 100):
            yield get_sum(str(a**b))


def get_sum(n: str):
    total = 0
    for i in n:
        total += int(i)
    return total


print(max(get_pow_and_get_digit_sum()))
