from typing import Any, Optional


class DecimalPart:
    def __init__(self, value: int, position: int) -> None:
        self.value = value
        self.position = position

    def __repr__(self) -> str:
        return f"DecimalPart({self.value}, {self.position})"


class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def append(self, value: Any) -> None:
        node = Node(value)
        self.size += 1

        if self.first is None:
            self.first = node
            self.last = self.first
            return

        self.last.next = node
        self.last = node

    def show(self) -> None:
        node = self.first
        while not (node is None):
            print(node.value)
            node = node.next

    def __getitem__(self, index) -> Any:
        node = self.first
        while index != 0:
            node = node.next
            index -= 1
        return node.value

    def __len__(self) -> int:
        return self.size


irrational_number = LinkedList()
position = 1
n = 0
while len(irrational_number) < (10**6):
    n += 1
    value = str(n)
    for char in value:
        decimal_part = DecimalPart(int(char), position)
        irrational_number.append(decimal_part)
        position += 1

result = 1
for i in range(7):
    result *= irrational_number[(10**i) - 1].value

print(result)
