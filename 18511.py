import sys

input = sys.stdin.readline

N, K_len = map(int, input().split())
K = sorted(map(int, input().split()), reverse=True)

N_len = len(str(N))

ans = 0

flag = False
def findNextHighest(num, depth):
    global ans
    global flag
    for digit in (K + [0] if depth == 0 else K):
        if flag:
            return
        num2check = num + digit * (10 ** (N_len - depth - 1))
        if num2check <= N:
            if depth == N_len - 1 and num2check > ans:
                ans = num2check
                flag = True
            else:
                findNextHighest(num2check, depth + 1)



findNextHighest(0, 0)

print(ans)
