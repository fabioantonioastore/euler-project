from functools import cache
from array import array
from typing import Any


class QueueDescriptor:
    def __set_name__(self, owner, name) -> None:
        self.storage_name = name

    def __get__(self, instance, owner) -> Any:
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value) -> None:
        instance.__dict__[self.storage_name] = value


class RotationQueue:
    values = QueueDescriptor()

    def __init__(self, values: list) -> None:
        self.values = values

    def __getitem__(self, index: int) -> Any:
        try:
            return self.values[index]
        except Exception as error:
            raise error

    def rotate(self, times: int = 1) -> None:
        for _ in range(times):
            first_value = self.values[0]
            self.values = self.values[1::]
            self.values.append(first_value)


class Circular:
    def __init__(self) -> None:
        pass

    @cache
    def is_prime(self, number: int) -> bool:
        if number % 2 == 0:
            return False

        square = int(number ** (1 / 2) + 1)
        for i in range(3, square, 2):
            if number % i == 0:
                return False

        return True

    def is_circular(self, number: int) -> bool:
        number_str = str(number)
        total_digits = len(number_str)
        number_rotations = self.get_rotations(number_str, total_digits)

        for number in number_rotations:
            if not self.is_prime(number):
                return False

        return True

    def get_rotations(self, number_str: str, digits: int) -> list[int]:
        rotation_queue = RotationQueue(list(number_str))
        rotation_numbers = []

        for _ in range(digits):
            rotation_number = ""
            for n in rotation_queue.values:
                rotation_number += n
            rotation_numbers.append(int(rotation_number))
            rotation_queue.rotate()

        return rotation_numbers


MAX_NUMBER = 10**6
CIRCULAR = Circular()
circular_primes = array("I", [2])

for n in range(3, MAX_NUMBER, 2):
    if CIRCULAR.is_circular(n):
        circular_primes.append(n)

print(circular_primes)
print(len(circular_primes))
