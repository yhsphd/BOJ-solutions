import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum([math.ceil(count / T) for count in sizes]))
print(N // P, N % P)
