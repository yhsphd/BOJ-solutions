import sys

input = sys.stdin.readline

coors = []

for i in range(int(input())):
    coors.append(list(map(int, input().split())))

coors = sorted(coors)

for coor in coors:
    print(f"{coor[0]} {coor[1]}")
