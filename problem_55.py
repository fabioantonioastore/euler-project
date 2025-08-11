from functools import cache


def is_polindrome(number: int) -> bool:
    return number == rev_number(number)


@cache
def rev_number(number: int) -> int:
    number = str(number)
    return int(number[-1:0:-1] + number[0])


MAX_ITERATION = 50


def is_lychrel(number: int) -> bool:
    for _ in range(MAX_ITERATION):
        number += rev_number(number)
        if is_polindrome(number):
            return False
    return True


MAX_RANGE = 10**4
total_lychrel = 0
for n in range(1, MAX_RANGE):
    if is_lychrel(n):
        total_lychrel += 1

print(total_lychrel)
