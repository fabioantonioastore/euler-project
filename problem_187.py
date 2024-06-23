from array import array

composite_primes = array("I")

class CompositePrimes:
    def __init__(self):
        pass

    def __repr__(self):
        return f"CompositePrimes()"
        
    def is_composite_prime(self, number: int) -> bool:
        if number in composite_primes:
            return True