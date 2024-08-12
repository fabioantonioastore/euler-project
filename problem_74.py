from array import array
from typing import NoReturn
from functools import reduce
from operator import mul

factorials = {
    1: 1,
    2: 2,
    3: 6
}

digit_factorials = {
    169: 363601,
    363601: 1454,
    1454: 169,
    871: 45361,
    45361: 871,
    872: 45362,
    45362: 872
}

def factorial(n: int) -> int:
    if n in factorials:
        return factorials[n]
    factorials[n] = reduce(mul, range(1, n + 1), 1)
    return factorials[n]

def get_fact_digit_sum(n: int) -> int:
    if n in digit_factorials:
        return digit_factorials[n]
    str_n = str(n)
    digit_factorials[n] = 0
    for i in str_n:
        digit_factorials[n] += factorial(int(i))
    return digit_factorials[n]

chains_terms = {
}

def create_chain(chain: array) -> int:
    if chain[-1] in chains_terms:
        if len(chain) == 1:
            return chains_terms[chain[-1]]
        return chains_terms[chain[-1]] + len(chain) - 1
    new_value = get_fact_digit_sum(chain[-1])
    if new_value in chain:
        chains_terms[chain[0]] = len(chain)
        return chains_terms[chain[0]]
    chain.append(new_value)
    return create_chain(chain)
    
total_sixty_chain = 0    
for i in range(2, 10 ** 6):
    if create_chain(array("I", [i])) == 60:
        total_sixty_chain += 1
print(total_sixty_chain)