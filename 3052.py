numbers = []
for i in range(10):
    numbers.append(int(input()))
res = set([x % 42 for x in numbers])
print(len(res))
