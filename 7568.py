import sys

input = sys.stdin.readline

people = []
rank = []

for _ in range(int(input())):
    people.append(tuple(map(int, input().split())))


def bigger(a, b):
    if a[0] < b[0] and a[1] < b[1]:
        return True
    return False


for person in people:
    count = 1
    for personCompare in people:
        if bigger(person, personCompare):
            count += 1
    rank.append(count)

print(" ".join(map(str, rank)))
