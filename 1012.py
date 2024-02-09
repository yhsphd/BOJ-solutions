import sys

input = sys.stdin.readline
sys.setrecursionlimit(3000)  # 1<=K<=2500


def rmGroup(fld, x, y):
    if fld[x][y] == 0:
        return fld

    fld[x][y] = 0
    if not x == 0:  # left
        fld = rmGroup(fld, x - 1, y)
    if not x == len(fld) - 1:  # right
        fld = rmGroup(fld, x + 1, y)
    if not y == 0:  # up
        fld = rmGroup(fld, x, y - 1)
    if not y == len(fld[x]) - 1:  # down
        fld = rmGroup(fld, x, y + 1)

    return fld


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0 for __ in range(N)] for ___ in range(M)]
    for __ in range(K):
        pt = list(map(int, input().split()))
        field[pt[0]][pt[1]] = 1  # input ready
    # print(field)

    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                count += 1
                field = rmGroup(field, i, j)

    print(count)
