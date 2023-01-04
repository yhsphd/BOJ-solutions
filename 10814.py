import sys
input = sys.stdin.readline

members = []
ans = []

for i in range(int(input())):
    member = input().split()
    members.append([int(member[0]), member[1]])

for i in range(201):
    for member in members:
        if member[0] == i:
            ans.append(member)

for answer in ans:
    print(f"{answer[0]} {answer[1]}")
