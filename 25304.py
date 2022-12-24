tot = int(input())
realtot = 0
count = int(input())

for i in range(count):
    item = input().split(" ")
    item = [int(x) for x in item]
    realtot += item[0]*item[1]

print("Yes" if tot == realtot else "No")