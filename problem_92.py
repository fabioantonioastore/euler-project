from array import array

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node({self.value!r}, {self.next!r}, {self.prev!r})"
    
class Chain:
    def __init__(self, value):
        self._values = array("I")
        self._size = 0
        self._endValue = self._calculation(value)

    def __repr__(self):
        return "Chain()"
    
    def __len__(self):
        return self._size
    
    def _calculation(self, value):
        if value == 89 or value == 1:
            self._values.append(value)
            self._size += 1
            return value
        if value in self._values:
            self._values.append(value)
            self._size += 1
            return value
        self._values.append(value)
        self._size += 1
        value = self._squareSum(value)
        return self._calculation(value)
    
    def getEndValue(self):
        return self._endValue
    
    def __str__(self):
        return str(self._values)

    def _squareSum(self, value):
        value = str(value)
        sum = 0
        for i in value:
            sum += int(i) ** 2
        return sum

resultValues = array("I")

for i in range(0, 10000000):
    value = Chain(i).getEndValue()
    print(value)
    if value == 89:
        resultValues.append(value)

print(resultValues)
print(len(resultValues))