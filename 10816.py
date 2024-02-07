from collections import Counter

input()
occr = Counter(sorted(input().split()))
input()
print(" ".join(map(str, [occr[n] for n in input().split()])))
