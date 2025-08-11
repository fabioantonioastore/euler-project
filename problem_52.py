from functools import partial


def get_product(mul: int, n: int) -> int:
    return n * mul


get_double = partial(get_product, 2)
get_triple = partial(get_product, 3)
get_quadruple = partial(get_product, 4)
get_five = partial(get_product, 5)
get_six = partial(get_product, 6)


def is_same_digits(n1: int, n2: int) -> bool:
    n1, n2 = str(n1), str(n2)
    if len(n1) == len(n2):
        return set(n1) == set(n2)
    return False


find = False
count = 1
while not (find):
    for i in range(2, 7):
        if is_same_digits(count, get_product(i, count)):
            if i == 6:
                print(count)
                find = True
        else:
            break
    count += 1
