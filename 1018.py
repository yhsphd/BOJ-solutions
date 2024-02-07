base = []
change = []
minimum = -1

# get input
for i in range(int(input().split()[0])):
    base.append([1 if c == "W" else 0 for c in input().strip()])

# count needed changes for each case
for i in (1, 0):
    start = i
    case = []
    for j in range(len(base)):
        case.append([int((start if k % 2 == 0 else not start) != base[j][k]) for k in range(len(base[j]))])
        start = not start
    change.append(case.copy())

for i in range(len(base) - 8 + 1):
    for j in range(len(base[i]) - 8 + 1):
        count = min([sum([sum(change[l][i + k][j:j + 8]) for k in range(8)]) for l in range(2)])
        if count == 0:      # if a case with no required changes is found, immediately print result and terminate
            print(0)
            exit()
        if minimum == -1 or minimum > count:
            minimum = count

# print(base)
# print(change)
print(minimum)
