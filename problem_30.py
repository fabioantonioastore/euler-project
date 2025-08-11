from array import array

totalNumbers = array("I")


def verify(number, power):
    numbers = (int(n) for n in str(number))
    sum = 0
    for n in numbers:
        sum += n**power
    if sum == number:
        totalNumbers.append(number)


for i in range(2, 1000000):
    verify(i, 5)

print(sum(totalNumbers))
