input()
numbers = input().split(" ")
numbers = [int(x) for x in numbers]
v = int(input())

count = 0
for num in numbers:
    if num == v:
        count += 1

print(count)
