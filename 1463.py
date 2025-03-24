"""import math
import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
ans = [-1] * (10 ** 6 + 1)
ans[1] = 0

def itr(num):
    if(num == 1):
        return 0
    elif(ans[num] >= 0):
        return ans[num]
    else:
        cnt = math.inf
        if(num % 3 == 0):
            cnt = min(cnt, itr(num // 3))
        if(num % 2 == 0):
            cnt = min(cnt, itr(num // 2))
        cnt = min(cnt, itr(num - 1))
        
        cnt += 1
        ans[num] = cnt
        return cnt

print(itr(N))
"""

n = int(input())
ans = [0] * (10 ** 6 + 1)

for i in range(2, n + 1):
    ans[i] = ans[i - 1] + 1
    if (i % 2 == 0):
        ans[i] = min(ans[i], ans[i // 2] + 1)
    if (i % 3 == 0):
        ans[i] = min(ans[i], ans[i // 3] + 1)

print(ans[n])