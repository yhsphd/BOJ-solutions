# 되도록 가격이 저렴할 때 최대한 많이 넣어야 한다.
# 더 저렴한 주유소를 만나기 전까지 그 다음으로 저렴한 주유소에서 채우기

import sys
input = sys.stdin.readline

N = int(input()) - 1
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))[:-1]  # 마지막 지역 가격은 필요X

totCost = 0
currCost = costs[0]
for i in range(N):
    if costs[i] < currCost:     # 가격이 낮아지는 순간 더 낮은 가격에 도달할 거리만큼 주유
        currCost = costs[i]
    totCost += currCost * dists[i]

print(totCost)
