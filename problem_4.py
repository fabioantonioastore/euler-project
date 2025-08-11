def pol(num):
    sNum = str(num)
    stack = []

    for i in sNum:
        stack.append(i)
    stack.reverse()

    for i in range(len(stack) - 1):
        if stack[i] != sNum[i]:
            return False
    return True


nums = []

for i in range(100, 1000):
    nums.append(i)
nums.reverse()

poli = []
for n1 in nums:
    for n2 in nums:
        if pol(n1 * n2):
            poli.append(n1 * n2)

print(max(poli))
