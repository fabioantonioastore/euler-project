class Triangular:
    def __init__(self, max_divisors: int) -> None:
        self.max_divisors = max_divisors
        self.natural = 1
        self.triangular = 1

    def __call__(self) -> int:
        while self.total_divisors(self.triangular) < self.max_divisors:
            next(self)
        return self.triangular

    def __next__(self) -> None:
        self.natural += 1
        self.triangular += self.natural

    def total_divisors(self, number: int) -> int:
        total_divisors = 1
        iteration = int(number ** (1 / 2))
        for n in range(1, iteration):
            if number % n == 0:
                total_divisors += 2
        return total_divisors

t = Triangular(500)
print(t())
