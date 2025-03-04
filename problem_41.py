from itertools import permutations


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return False
    
    root = int(number ** (1 / 2))
    for n in range(3, root + 1, 2):
        if number % n == 0:
            return False
    
    return True


def get_permutations(digits: str) -> list[int]:
    numbers = []
    for tp in permutations(digits):
        number = ""
        for digit in tp:
            number += digit
        numbers.append(int(number))
    
    return sorted(numbers, reverse=True)


digits = "123456789"
max_prime = 0
while max_prime == 0:
    numbers = get_permutations(digits)
    for n in numbers:
        if is_prime(n):
            max_prime = n
            break
    
    digits = digits[0:-1:]

print(max_prime)