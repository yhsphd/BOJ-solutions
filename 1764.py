import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

d = set()
b = set()

for _ in range(N):
    d.add(input().strip())

for _ in range(M):
    b.add(input().strip())

db = d.intersection(b)
print(len(db))
print("\n".join(sorted(db)))