def find(n,m1,m2):
    sum = 0
    for i in range(n):
        if i % m1 == 0:
            sum += i
        elif i % m2 == 0:
            sum += i
    return sum

print(find(1000,3,5))