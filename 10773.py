import sys

numbers = []
K = int(sys.stdin.readline().rstrip())

for i in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))
