data = {1: 1, 2: 1}


def fibonnaci(value):
    if value in data:
        return data[value]
    data[value] = fibonnaci(value - 1) + fibonnaci(value - 2)
    return data[value]


count = 1
while True:
    if len(str(fibonnaci(count))) != 1000:
        count += 1
    else:
        break

print(count)
