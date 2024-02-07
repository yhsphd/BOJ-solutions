import sys

input = sys.stdin.readline

n = int(input())
ratings = []

if n == 0:
    print(0)
    exit()

for _ in range(n):
    ratings.append(int(input()))

ign = int(n * 0.15 + 0.5)  # python3 rounding
# print(ign)
# print(sorted(ratings))
if ign > 0:
    ratings = sorted(ratings)[ign:-ign]
# print(ratings)
print(int(sum(ratings) / len(ratings) + 0.5))
