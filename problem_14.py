sequence = {1:1}

# even, n -> n/2
# odd, n -> 3n + 1

def collatz(value):
    if value in sequence:
        return sequence[value]
    sequence[value] = evaluete(value)
    return sequence[value]

def evaluete(value, count=1):
    if value == 1:
        return count
    if value % 2 == 1:
        return evaluete((value * 3) + 1, count + 1)
    else:
        return evaluete(value / 2, count + 1)
    
l = []
for i in range(1, 1000000):
    l.append(collatz(i))

maxValue = max(l)
print(l.index(maxValue) + 1)