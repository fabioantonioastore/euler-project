primes = [2, 3, 5, 7, 11, 13, 17]


def get_pandigitals(numbers: list[str]):
    for a in numbers:
        numbers_a = numbers.copy()
        numbers_a.remove(a)
        for b in numbers_a:
            numbers_b = numbers_a.copy()
            numbers_b.remove(b)
            for c in numbers_b:
                numbers_c = numbers_b.copy()
                numbers_c.remove(c)
                for d in numbers_c:
                    numbers_d = numbers_c.copy()
                    numbers_d.remove(d)
                    for e in numbers_d:
                        numbers_e = numbers_d.copy()
                        numbers_e.remove(e)
                        for f in numbers_e:
                            numbers_f = numbers_e.copy()
                            numbers_f.remove(f)
                            for g in numbers_f:
                                numbers_g = numbers_f.copy()
                                numbers_g.remove(g)
                                for h in numbers_g:
                                    numbers_h = numbers_g.copy()
                                    numbers_h.remove(h)
                                    for i in numbers_h:
                                        numbers_i = numbers_h.copy()
                                        numbers_i.remove(i)
                                        for j in numbers_i:
                                            yield a + b + c + d + e + f + g + h + i + j


pandigitals = 0
for n in get_pandigitals(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
    if not (int(n[1:4:]) % 2 == 0):
        continue
    if not (int((n[2:5:])) % 3 == 0):
        continue
    if not (int(n[3:6:]) % 5 == 0):
        continue
    if not (int(n[4:7:]) % 7 == 0):
        continue
    if not (int(n[5:8:]) % 11 == 0):
        continue
    if not (int(n[6:9:]) % 13 == 0):
        continue
    if not (int(n[7:10:]) % 17 == 0):
        continue
    pandigitals += int(n)

print(pandigitals)
