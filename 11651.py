import sys

input = sys.stdin.readline

coors = []

for i in range(int(input())):
    coors.append(list(map(int, input().split()[::-1])))

coors = sorted(coors)

for coor in coors:
    print(f"{coor[1]} {coor[0]}")
