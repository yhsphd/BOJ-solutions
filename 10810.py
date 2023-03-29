mn = list(map(int, input().split()))

baskets = [0] * mn[0]

for i in range(mn[1]):
    ijk = list(map(int, input().split()))
    for j in range(ijk[0] - 1, ijk[1]):
        baskets[j] = ijk[2]

print(" ".join(map(str, baskets)))
