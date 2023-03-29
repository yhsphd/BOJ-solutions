num = [input(), input()]
ans = []

for i in range(len(num[1])):
    print(int(num[0]) * int(num[1][-1 - i]))

print(int(num[0]) * int(num[1]))
