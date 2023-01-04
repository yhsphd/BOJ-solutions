import sys
input = sys.stdin.readline

unique = {}

input()
nums = list(map(int, input().split()))
uniquenums = sorted(set(nums))

unique = {uniquenums[i]: i for i in range(len(uniquenums))}

for num in nums:
    print(unique[num], end=" ")
