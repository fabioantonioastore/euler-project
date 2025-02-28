from typing import Any
from functools import cache


@cache
def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return False

    root = int((number ** (1 / 2)))

    for n in range(3, root + 1, 2):
        if number % n == 0:
            return False
    return True


class SpiralDescriptor:
    def __set_name__(self, owner, name) -> None:
        self.storage_name = name

    def __get__(self, instance, owner) -> Any:
        return instance.__dict__[self.storage_name]
        
    def __set__(self, instance, value) -> None:
        instance.__dict__[self.storage_name] = value


class Spiral:
    diagonals = SpiralDescriptor()

    def __init__(self, layers: int | None) -> None:
        self.diagonals = [1]
        self.total_primes = 0
        self.total_diagonals = 1
        if layers and (layers % 2 != 0):
            deepth = int((layers - 1) / 2)
            for _ in range(deepth):
                self.add_layer()

    def add_layer(self) -> None:
        last_number = self.diagonals[-1]
        deepth = self.calc_deepth() + 1
        for _ in range(4):
            sloop = deepth * 2
            number = last_number + sloop
            self.diagonals.append(number)
            last_number = self.diagonals[-1]
            if is_prime(number):
                self.total_primes += 1
        self.total_diagonals += 4


    def calc_deepth(self) -> int:
        total_layers = self.get_total_layers()
        deepth = int((total_layers - 1) / 2)
        return deepth

    def get_total_layers(self) -> int:
        last_number = self.diagonals[-1]
        if last_number == 1:
            return 1
        return int(last_number ** (1 / 2))
            
    def calc_ratio(self) -> float:
        return self.total_primes / self.total_diagonals
    
SPIRAL = Spiral(7)
while SPIRAL.calc_ratio() >= 0.10:
    SPIRAL.add_layer()

print(SPIRAL.get_total_layers())