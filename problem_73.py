def gcd(n1: int, n2: int) -> int:
    while n2 != 0:
        temp = n2
        n2 = n1 % n2
        n1 = temp
    return n1


f1 = 1 / 3
f2 = 1 / 2
total = 0
for d in range(2, 12_001):
    for n in range(1, d):
        if gcd(n, d) == 1:
            fraction_value = n / d
            if f1 < fraction_value < f2:
                total += 1

print(total)