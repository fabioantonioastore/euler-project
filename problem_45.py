# T = n(n + 1) / 2
# n = (-1 + ((1 + 8T) ** (1 / 2))) / 2

# P = n(3n - 1) / 2
# n = (1 + ((1 + 24P) ** (1 / 2))) / 6

# H = n(2n - 1)
# n = (1 + ((1 + 8H) ** (1 / 2))) / 4


def rev_triangle(n: int) -> int:
    sqrt = (1 + (8 * n)) ** (1 / 2)
    return (-1 + sqrt) / 2


def rev_pentagonal(n: int) -> int:
    sqrt = (1 + (24 * n)) ** (1 / 2)
    return (1 + sqrt) / 6

def rev_hexagonal(n: int) -> int:
    sqrt = (1 + (8 * n)) ** (1 / 2)
    return (1 + sqrt) / 4

n = 40756
while True:
    rev_t = rev_triangle(n)
    if not (int(rev_t) == rev_t):
        n += 1
        continue

    rev_p = rev_pentagonal(n)
    if not (int(rev_p) == rev_p):
        n += 1
        continue

    rev_h = rev_hexagonal(n)
    if not (int(rev_h) == rev_h):
        n += 1
        continue

    print(n)
    break