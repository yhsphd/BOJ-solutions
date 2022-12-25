field = [[False for i in range(100)] for j in range(100)]

for i in range(int(input())):
    pos = list(map(int, input().split()))
    for j in range(10):
        for k in range(10):
            field[pos[0]+j][pos[1]+k] = True
print(sum(sum(field, [])))
