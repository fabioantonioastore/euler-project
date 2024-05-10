from array import array
import cython

class Node:
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def __repr__(self):
        return f"Node({self._value!r})"
    
    def getNext(self):
        return self._next
    
    def getValue(self):
        return self._value
    
    def setNext(self, next):
        self._next = next
    
class Stack:
    def __init__(self, value=None):
        if value == None:
            self._size = 0
        else:
            self._last = Node(value)
            self._first = self._last
            self._size = 1
        
    def __repr__(self):
        return f"Stack({self._last.getValue()!r})"
    
    def __len__(self):
        return self._size
    
    def add(self, value):
        if len(self) == 0:
            self._last = Node(value)
            self._first = self._last
            self._size += 1 
        else:
            node = Node(value)
            node.setNext(self._first)
            self._first = node
            self._size += 1
    
    def pop(self):
        if len(self) == 0:
            return None
        else:
            node = self._first
            self._first = self._first.getNext()
            value = node.getValue()
            del node
            return value
    
    def getCurrent(self):
        try:
            return self._first.getValue()
        except:
            return None
        
def getReverseValue(value):
    temp = Stack()
    for v in str(value):
        temp.add(v)
    value = ""
    while temp.getCurrent() != None:
        value += temp.pop()
    return int(value)

primes = array("I", [2, 3, 5, 7])
reversibles = array("I")
squarePrimes = {
    2: 4,
    3: 9,
    5: 25,
    7: 49
}

@cython.locals(value=cython.int)
def isPolidrome(value):
    if value == getReverseValue(value):
        return True
    return False

@cython.locals(value=cython.int, p=cython.int)
def getPrime(value):
    for p in primes:
        if value % p == 0:
            return
    primes.append(value)
    squarePrimes[value] = value ** 2

@cython.locals(value=cython.int, n=cython.int)
def isPrime(value):
    if value > primes[-1]:
        for n in range(primes[-1], value + 1, 2):
            getPrime(n)
    if value in primes:
        return True
    return False

@cython.locals(value=cython.int, p=cython.int)
def isPrimeSquare(value):
    if isPrime(value):
        return False
    for p in primes:
        if value == squarePrimes[p]:
            return True
    return False

@cython.locals(value=cython.int, rValue=cython.int)
def getReversibles(value):
    if isPrime(value):
        return
    if not(isPolidrome(value)) and isPrimeSquare(value):
        rValue = getReverseValue(value)
        if rValue in reversibles:
            reversibles.append(value)
            return
        if not(isPolidrome(rValue)) and isPrimeSquare(rValue):
            if not(value in reversibles):
                reversibles.append(value)

count = 3
while len(reversibles) != 50:
    getReversibles(count)
    count += 2

print(sum(reversibles))