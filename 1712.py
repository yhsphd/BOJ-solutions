num = list(map(int, input().split(" ")))

if num[1] >= num[2]:
    print(-1)
else:
    print(num[0] // (num[2] - num[1]) + 1)
