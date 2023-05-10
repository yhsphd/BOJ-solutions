from collections import deque

N, K = map(int, input().split())

numbers = deque(range(1, N + 1))
ans = []

while (len(numbers) != 0):
    for i in range(K - 1):
        numbers.append(numbers.popleft())
    ans.append(numbers.popleft())

print(f'<{", ".join(map(str, ans))}>')
