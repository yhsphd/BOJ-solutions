max = 0
ind = 0

for i in range(9):
    num = int(input())
    if max < num:
        max = num
        ind = i + 1

print(max)
print(ind)
