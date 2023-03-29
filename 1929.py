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


M, N = map(int, input().split())

for i in range(M, N + 1):
    if checkPrime(i):
        print(i)
