factorialData = {1: 1, 2: 2, 3: 6}


def factorial(n):
    if n in factorialData:
        return factorialData[n]
    factorialData[n] = n * factorial(n - 1)
    return factorialData[n]


result = (int(n) for n in str(factorial(100)))
print(sum(result))
