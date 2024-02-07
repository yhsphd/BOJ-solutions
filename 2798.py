import itertools

_, M = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

maximum = -1

for case in itertools.combinations(cards, 3):
    hap = sum(case)
    if hap == M:
        print(M)
        exit()
    if maximum < hap <= M:
        maximum = sum(case)

print(maximum)
