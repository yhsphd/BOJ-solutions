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


primes = []

for i in range(int(input()), int(input()) + 1):
    if checkPrime(i):
        primes.append(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
