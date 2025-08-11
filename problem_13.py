FILE_NAME = "problem_13.txt"


def get_numbers() -> list[int]:
    numbers = []
    with open(FILE_NAME, "r") as file:
        for n in file.readlines():
            numbers.append(int(n))
    return numbers


print(str(sum(get_numbers()))[0:10:])
