MIN_INTERVAL = 2
MAX_INTERVAL = 100
numbers: set = set()

for a in range(MIN_INTERVAL, MAX_INTERVAL + 1):
    for b in range(MIN_INTERVAL, MAX_INTERVAL + 1):
       numbers.add(a ** b)
print(len(numbers))