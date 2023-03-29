A = []
h = 0
pos = [0, 0]

for i in range(9):
    A.append(list(map(int, input().split())))
    m = max(A[-1])
    if m > h:
        h = m
        pos = [i, A[i].index(m)]

print(f"{h}\n{pos[0] + 1} {pos[1] + 1}")
