PRIME = (28433 * pow(2, 7830457)) + 1
TOTAL_DIGITS = 2357207


def get_digits(digits_amount: int = 1) -> int:
    if digits_amount < 1:
        raise "error"
    digits_amount -= 1
    return PRIME // pow(10, TOTAL_DIGITS - 1 - digits_amount)


def get_digit_in_position(position: int) -> int:
    digits = get_digits(position)
    return digits - (get_digits(position - 1) * 10)


ten_digits = ""
for i in range(9, -1, -1):
    digit_position = TOTAL_DIGITS - i
    ten_digits += str(get_digit_in_position(digit_position))

print(ten_digits)
