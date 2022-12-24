X = int(input().split(" ")[1])
A = input().split(" ")
A = [int(x) for x in A]

for num in A:
    if num < X:
        print(num, end=" ")
