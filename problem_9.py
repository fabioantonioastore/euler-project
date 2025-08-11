def find(value):
    for a in range(value):
        for b in range(value):
            if a < b:
                for c in range(value):
                    if (
                        b < c
                        and pow(a, 2) + pow(b, 2) == pow(c, 2)
                        and a + b + c == value
                    ):
                        return (a, b, c)
                    continue


product = 1
for i in find(1000):
    product *= i

print(product)
