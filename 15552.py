import sys
input = sys.stdin.readline

count = int(input())

for i in range(count):
    num = input().split(" ")
    num = [int(x) for x in num]
    print(num[0]+num[1])
