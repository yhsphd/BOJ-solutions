import sys

input = sys.stdin.readline

"""
구역 분할
1   2
3   4
"""


def findZ(size, r, c, start):
    if size == 0:   # 종료조건
        return start
    if r >= 2 ** (size - 1):
        if c >= 2 ** (size - 1):  # 4영역
            return findZ(size - 1, r - 2 ** (size - 1), c - 2 ** (size - 1), start + (4 ** (size - 1)) * 3)
            # 사이즈 반으로 감소, 행렬 이동, 시작번호 이동
        else:  # 3영역
            return findZ(size - 1, r - 2 ** (size - 1), c, start + (4 ** (size - 1)) * 2)
    else:
        if c >= 2 ** (size - 1):  # 2영역
            return findZ(size - 1, r, c - 2 ** (size - 1), start + (4 ** (size - 1)) * 1)
        else:  # 1영역
            return findZ(size - 1, r, c, start)


N, r, c = map(int, input().split())
print(findZ(N, r, c, 0))
