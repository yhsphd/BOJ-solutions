import math


def checkPrime(num: int):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(math.floor(math.sqrt(num))):
            if i == 0:
                continue
            elif num % (i + 1) == 0:
                return False
        return True


input()
numbers = list(map(int, input().split()))

count = 0
for num in numbers:
    count += checkPrime(num)

print(count)
