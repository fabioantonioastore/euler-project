def is_polindrome(number: int) -> bool:
    number = str(number)
    return number == (number[-1:0:-1] + number[0])

def to_bin(number: int) -> str:
    return str(bin(number))[2::]

total_sum = 0
MAX_RANGE = 10 ** 6

for n in range(1, MAX_RANGE):
    if is_polindrome(n) and is_polindrome(to_bin(n)):
        total_sum += n

print(total_sum)