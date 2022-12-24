cases = int(input())
ans = []

for i in range(cases):
    num = input().split(" ")
    num = [int(x) for x in num]
    ans.append(num[0] + num[1])

for x in ans:
    print(x)
