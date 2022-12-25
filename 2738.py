N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))

ans = ""

for i in range(N):
    for j in range(M):
        ans += f"{A[i][j] + B[i][j]} "
    ans = ans.rstrip()
    ans += "\n"
ans = ans.rstrip()

print(ans)
