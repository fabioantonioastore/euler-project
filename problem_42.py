from functools import cache


FILE_NAME = "problem_42.txt"


def get_words() -> list[str]:
    result = []
    with open(FILE_NAME, "r") as file:
        for line in file.readlines():
            words = line.split(",")
            for word in words:
                result.append(word[1:-1:])

    return result


@cache
def get_letter_position(letter: str) -> int:
    return ord(letter) - ord("A") + 1


def get_word_value(word: str) -> int:
    value = 0
    for letter in word:
        value += get_letter_position(letter)

    return value


@cache
def triangule_number(term: int) -> int:
    return (term / 2) * (term + 1)


def is_triangule_word(word: str) -> bool:
    word_value = get_word_value(word)
    term = 1

    while True:
        triangule = triangule_number(term)
        if triangule == word_value:
            return True
        if triangule > word_value:
            return False
        term += 1


words = get_words()
total_triangule_words = 0

for word in words:
    if is_triangule_word(word):
        total_triangule_words += 1

print(total_triangule_words)
