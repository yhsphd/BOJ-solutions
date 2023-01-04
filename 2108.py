import math
import sys
input = sys.stdin.readline

count = [0]*8001
"""
-4000   0       4000
0       4000    8000
"""

# 입력
N = int(input())

for i in range(N):
    count[int(input())+4000] += 1

ans = [None]*4
# 산술평균, 중앙값, 최빈값, 범위

tot = 0
ind = 0
maxocc = max(count)
mode = []
minnum = None
maxnum = None

for i in range(8001):
    tot += (i-4000) * count[i]
    ind += count[i]
    if ind >= (N+1)//2 and ans[1] == None:
        ans[1] = i-4000
    if count[i] == maxocc:
        mode.append(i-4000)
    if count[i] != 0:
        maxnum = i-4000
        if minnum == None:
            minnum = i-4000

mode = sorted(mode)

ans[0] = int(tot/N + 0.5) if tot >= 0 else int(tot/N - 0.5)
ans[2] = mode[0] if len(mode) == 1 else mode[1]
ans[3] = maxnum - minnum

for ansnum in ans:
    print(ansnum)
