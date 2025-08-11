permutations = []

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

MAX_LEN = len(numbers)


def _get_permutations(value: str) -> None:
    if len(value) == MAX_LEN:
        permutations.append(value)
        return
    for i in numbers:
        if i in value:
            continue
        _get_permutations(value + i)


def get_permutations() -> None:
    for i in numbers:
        _get_permutations(i)


MILLION = 10**6
MIL = 10**3
get_permutations()
print(permutations[MILLION - 1])
