from functools import cache


@cache
def get_letter_position(letter: str) -> int:
    return ord(letter) - ord("A") + 1


FILE_NAME = "problem_22.txt"


def get_names() -> list[str]:
    names = []
    with open(FILE_NAME, "r") as file:
        for line in file.readlines():
            for name in line.split(","):
                names.append(name[1:-1:])
    return names


def total_names_score(names: list[str]) -> int:
    total_score = 0
    index = 1
    for name in names:
        letter_score = 0
        for letter in name:
            letter_score += get_letter_position(letter)
        total_score += letter_score * index
        index += 1
    return total_score


names = get_names()
names.sort()
print(total_names_score(names))
