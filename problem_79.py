succesful_attemps = []
digits_in_passcode = set()

with open("problem_79.txt") as file:
    for line in file:
        succesful_attemps.append([str(i) for i in line[:-1:]])
        for digit in line[:-1:]:
            digits_in_passcode.add(digit)


def is_valid_combination(passcode: list[str], combination: list[str]) -> bool:
    for digit in combination:
        if not digit in passcode:
            return False

    index_one = passcode.index(combination[0])
    index_two = passcode.index(combination[1])
    index_three = passcode.index(combination[2])

    if index_one < index_two < index_three:
        return True
    if passcode.count(combination[0]) == 1 and passcode.count(combination[1]) == 1 and passcode.count(
            combination[2]) == 1:
        return False

    for i in range(len(passcode)):
        if passcode[i] == combination[2] and i > index_three:
            index_three = i
            continue
    for i in range(len(passcode)):
        if passcode[i] == combination[1] and index_one < i < index_three:
            index_two = i
            break

    return index_one < index_two < index_three


def generate_passcode(digits: list[str], passcode: list[str]):
    if not digits:
        yield passcode
    for digit in digits:
        new_digits = digits.copy()
        new_passcode = passcode.copy()
        new_passcode.append(digit)
        new_digits.remove(digit)
        yield from generate_passcode(new_digits, new_passcode)


def list_to_str(str_list: list[str]) -> str:
    string = ""
    for letter in str_list:
        string += letter
    return string


passcode_len = None
final_passcode = None
for passcode in generate_passcode(list(digits_in_passcode), []):
    valid = True
    for combination in succesful_attemps:
        if not is_valid_combination(passcode, combination):
            valid = False
            break
    if valid:
        if not passcode_len:
            passcode_len = len(passcode)
            final_passcode = list_to_str(passcode)
            continue
        if len(passcode) < passcode_len:
            passcode_len = len(passcode)
            final_passcode = list_to_str(passcode)
            continue


print(final_passcode)
