def pow(value, expoent):
    result = value
    count = 1
    while count != expoent:
        result *= 2
        count += 1
    return result


numbers = str(pow(2, 1000))
sum = 0

for i in numbers:
    sum += int(i)

print(sum)
