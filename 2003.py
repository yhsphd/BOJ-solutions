import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0
Psum = [0]
for i in range(N):
    Psum.append(Psum[-1] + numbers[i])

for i in range(N + 1):
    for j in range(i + 1, N + 1):
        if Psum[j] - Psum[i] == M:
            count += 1

print(count)
