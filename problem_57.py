from functools import cache
from typing import Any
from sys import setrecursionlimit


setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value: Any, next: 'Node' = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r}, {self.next!r})"


class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.top = None
        self.__iter_stack = None

    def append(self, item: Any) -> None:
        node = Node(item)
        self.size += 1
        if self.top is None:
            self.top = node
            return
        node.next = self.top
        self.top = node

    def pop(self) -> Any:
        self.size -= 1
        node = self.top
        self.top = node.next
        return node.value

    def __len__(self) -> int:
        return self.size

    def __list__(self) -> list[Any]:
        node = self.top
        l = []
        while not node is None:
            l.append(node.value)
            node = node.next
        return l

    def __iter__(self) -> 'Stack':
        if not self.__iter_stack:
            self.__iter_stack = Stack()
        self.__iter_stack.append(self.top)
        return self

    def __next__(self) -> Any:
        node = self.__iter_stack.top.value
        if node is None:
            self.__iter_stack.pop()
            raise StopIteration
        self.__iter_stack.top.value = node.next
        return node.value

    def __repr__(self) -> str:
        return f"Stack({list(self)!r})"


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self) -> None:
        mdc_n = mdc(self.numerator, self.denominator)
        self.numerator = self.numerator // mdc_n
        self.denominator = self.denominator // mdc_n

    def __add__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(
            (self.numerator * other.denominator) + (other.numerator * self.denominator),
            self.denominator * other.denominator
        )

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __repr__(self) -> str:
        return f"Fraction({self.numerator!r}, {self.denominator!r})"


def mdc(n1: int, n2: int) -> int:
    while n2 != 0:
        t = n2
        n2 = n1 % n2
        n1 = t
    return n1


@cache
def convergent(depth: int, fraction: Fraction = Fraction(1,2 )) -> Fraction:
    if depth == 1:
        return Fraction(1, 1) + fraction

    fraction = fraction + Fraction(2, 1)
    fraction = Fraction(1, 1) * Fraction(fraction.denominator, fraction.numerator)

    return convergent(depth - 1, fraction)


def get_digits(n: int) -> int:
    div = 1
    total = 1
    while True:
        if n % (10 ** div) == n:
            return total
        div += 1
        total += 1


total = 0
for i in range(1, 1001):
    fraction = convergent(i)
    if get_digits(fraction.numerator) > get_digits(fraction.denominator):
        total += 1

print(total)