import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

A.sort()

for find in num:
    flag = False

    lo, hi = -1, N + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if A[mid] < find:
            lo = mid
        elif A[mid] > find:
            hi = mid
        elif A[mid] == find:
            flag = True
            break

    print(int(flag))
