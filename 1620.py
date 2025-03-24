import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n2i = {}
i2n = [""]

for i in range(1, N + 1):
    name = input().strip()
    n2i[name] = i
    i2n.append(name)

for _ in range(M):
    req = input().strip()
    print(i2n[int(req)] if req.isnumeric() else n2i[req])