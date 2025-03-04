from functools import cache, lru_cache


@cache
def is_prime(number: int) -> bool:
    if number == 2:
        return True

    if number % 2 == 0 or number == 1:
        return False

    root = int(number ** (1 / 2) + 1)
    for n in range(3, root, 2):
        if number % n == 0:
            return False

    return True


@lru_cache
def remove_left(number: int) -> int:
    return int(str(number)[1::])


@lru_cache
def remove_right(number: int) -> int:
    return int(str(number)[0:-1:])


def get_total_digits(number: int) -> int:
    return len(str(number))


def is_truncatable(number: int) -> bool:
    if not is_prime(number):
        return False

    total_digits = get_total_digits(number)

    left = number
    right = number

    for _ in range(total_digits - 1):
        left = remove_left(left)
        right = remove_right(right)

        if is_prime(left) and is_prime(right):
            continue

        return False

    return True


total_sum = 0
number = 11
TOTAL = 11
founds = 0


while founds < TOTAL:
    if is_truncatable(number):
        total_sum += number
        founds += 1

    number += 2

print(total_sum)