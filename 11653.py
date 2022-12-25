import math
import sys


def checkPrime(num: int):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(math.floor(math.sqrt(num))):
            if i == 0:
                continue
            elif num % (i+1) == 0:
                return False
        return True


input = sys.stdin.readline
num = int(input())

if num == 1:
    pass
elif checkPrime(num):
    print(num)
else:
    x = 2
    while num != 1:
        if num % x == 0:
            print(x)
            num = num//x
            x = 2
        else:
            x += 1
