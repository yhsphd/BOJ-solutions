initial = 100

N = int(input())
pool = set(range(10))  # 0-9
if input() != "0":
    for n in map(int, input().split()):
        pool.remove(n)
# print(pool)
# input ready

ans = []

# case 1: only using +/-
ans.append(abs(initial - N))

# case 2: using both
if len(pool) == 0:  # if there's no button left, only use ans1
    print(ans[0])
    exit()

digits = len(str(N))
# case 2-1: from below
for i in range(N + 1).__reversed__():
    if set(map(int, str(i))).issubset(pool):
        ans.append(len(str(i)) + abs(i - N))
        break
# case 2-2: from above
i = N
if pool != {0}:
    while True:
        if set(map(int, str(i))).issubset(pool):
            ans.append(len(str(i)) + abs(i - N))
            break
        i += 1

print(min(ans))
