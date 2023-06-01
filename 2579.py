import sys

input = sys.stdin.readline

H = int(input())
points = [0]

for i in range(H):
    points.append(int(input()))

"""
def step(current, score, seq):
    if current > H:
        return 0

    score += points[current]

    high1 = 0
    high2 = 0

    if current == H:
        return score
    else:
        high2 = step(current + 2, score, 1)
        if seq != 2:
            high1 = step(current + 1, score, seq + 1)

    return high1 if high1 > high2 else high2


print(step(0, 0, 0))
"""

if H == 1:
    print(points[1])
    quit()

# Initialize
DP = [[0, 0] for _ in range(H + 1)]
# DP[n][0]: 마지막에 1칸 뛰었을 때, DP[n][1]: 마지막에 2칸 뛰었을 때 n번째 계단에서 얻는 최대 점수
DP[1][0] = points[1]
DP[2] = [points[1] + points[2], points[2]]

if H == 2:
    print(max(DP[H]))
    quit()

# DP
for current in range(3, H + 1):
    # H-2번째 계단에서 H로 올라오는 경우
    DP[current][1] = max(DP[current - 2]) + points[current]
    # H-1번째 계단에서 H로 올라오는 경우
    DP[current][0] = DP[current - 1][1] + points[current]

print(max(DP[H]))
