from typing import NoReturn
from array import array
    
class Prime:
    def __init__(self) -> NoReturn:
        self.primes = array("I", [2, 3, 5, 7])

    def is_prime(self, n: int) -> bool:
        return self.calc_prime(n)

    def calc_prime(self, n: int) -> bool:
        if n in self.primes: return True
        if n < self.primes[-1] or n % 2 == 0: return False
        max_prime = self.primes[-1]
        for i in range(max_prime + 2, n + 1, 2):
            find = True
            for prime in self.primes:
                if i % prime == 0:
                    find = False
                    break
            if find:
                self.primes.append(i)
        return n in self.primes

    def __call__(self, n: int) -> bool:
        return self.is_prime(n)
    
    def get_primes_in_list(self) -> list:
        return self.primes.tolist()
    
    def get_primes_in_array(self) -> array:
        return self.primes

class Generate:
    def __init__(self) -> NoReturn:
        self.PRIME = Prime()

    def generate_from_number(self, n: int) -> bool:
        self.PRIME(n)
        max_sqrt = self.get_sqrt_max(n)
        for prime in self.PRIME.get_primes_in_array():
            if prime > n:
                break
            for i in range(max_sqrt, 0, -1):
                if self.calc_composite((prime, i)) == n: return True
        return False
    
    def calc_composite(self, n: tuple[int]) -> int:
        return n[0] + (2 * (n[1] ** 2))    

    def get_sqrt_max(self, n: int) -> int:
        n = (n - 1) / 2
        return int((n ** (1/2)) // 1)

    def valid_number(self, n: int) -> bool:
        return self.generate_from_number(n)
    
    def is_prime(self, n: int) -> bool:
        return self.PRIME(n)
    
    def __call__(self, n: int) -> bool:
        return self.valid_number(n)
    
number = 3
GENERATE = Generate()
while True:
    if GENERATE.is_prime(number):
        number += 2
        continue
    if not(GENERATE(number)): break
    number += 2

print(number)