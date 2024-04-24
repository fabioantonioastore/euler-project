sequence = {1:1}

# even, n -> n/2
# odd, n -> 3n + 1

def collatz(value):
    if value in sequence:
        return sequence[value]
    if value % 2 == 1:
        value = (3 * value) + 1
        sequence[value] = 1 + collatz(value)
        return sequence[value]
    else:
        value = value / 2
        sequence[value] = 1 + collatz(value)
        return sequence[value]
 
l = []
for i in range(1, 1000000):
    l.append(collatz(i))

maxValue = max(l)
print(l.index(maxValue) + 1)