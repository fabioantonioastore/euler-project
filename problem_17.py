letters = {
    "100": "hundred",
    "1000": "thousand",
    "and": "and",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety",
}


def get_len_number(number: str) -> int:
    return len(letters[number])


total_letters = 0


def get_len(i: int) -> None:
    global total_letters
    if i == 1000:
        total_letters += get_len_number("1") + get_len_number("1000")
        return
    if i % 100 == 0:
        i = str(i)
        total_letters += get_len_number(i[0]) + get_len_number("100")
        return

    i = str(i)

    if len(i) == 3:
        total_letters += (
            get_len_number(i[0]) + get_len_number("100") + get_len_number("and")
        )
        i = i[1::]

    if len(i) == 2:
        if not (i[0] == "0"):
            if int(i) >= 20:
                total_letters += get_len_number(i[0] + "0")
            else:
                total_letters += get_len_number(i)
                return

        i = i[1::]

    if len(i) == 1:
        if i == "0":
            return
        total_letters += get_len_number(i)


for i in range(1, 1001):
    get_len(i)

print(total_letters)
