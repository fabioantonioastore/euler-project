from sys import setrecursionlimit

setrecursionlimit(10000)

powValues = {1: 1, 2: 4}


class Pow:
    def __init__(self, value):
        self._values = []
        self._sum = 0
        self._calculation(value)

    def _calculation(self, value):
        if value == 0:
            return
        match value in powValues:
            case 1:
                self._values.append(powValues[value])
                return self._calculation(value - 1)
            case 0:
                powValues[value] = self._pow(value, value)
                self._values.append(powValues[value])
                return self._calculation(value - 1)

    def _pow(self, value, times=1):
        result = value
        for _ in range(times - 1):
            result *= value
            if len(str(result)) > 10:
                result = int(str(result)[-10:])
        return result

    def getSum(self):
        if self._sum:
            return self._sum
        for value in self._values:
            self._sum += value
        return self._sum


result = Pow(1000).getSum()
if len(str(result)) > 10:
    result = int(str(result)[-10:])
print(result)
