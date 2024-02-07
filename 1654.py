import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

m, n = 1, max(lines)
count = 0
key = (m + n) // 2


def check(num):
    return sum([line // num for line in lines])


while True:
    count = check(key)
    if count >= N:
        m = key
        key = (m + n) // 2
    else:
        n = key
        key = (m + n) // 2
    if m == key or key == n:
        if check(n) >= N:
            key = n
        break

print(key)
