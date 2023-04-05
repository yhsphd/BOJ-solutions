import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def findAnother(seq):
    if len(seq) == M:
        print(" ".join(map(str, seq)))
    elif seq[-1] > N:
        return
    else:
        for i in range(1, N + 1):
            findAnother(seq + [i])


for i in range(1, N + 1):
    findAnother([i])
