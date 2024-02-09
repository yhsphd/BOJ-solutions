import sys

input = sys.stdin.readline

fibCount = [[1, 0], [0, 1]]

for _ in range(40 - 1):  # prepare for case N=0 to N=40 before getting input
    fibCount.append([fibCount[-1][0] + fibCount[-2][0], fibCount[-1][1] + fibCount[-2][1]])

for _ in range(int(input())):
    print(" ".join(map(str, fibCount[int(input())])))
