import math

MAX = 10001
prime = [True]*MAX
prime[1] = False
primes = []

for i in range(2, math.floor(math.sqrt(MAX))+1):
    if prime[i]:
        for j in range(i*2, MAX, i):
            prime[j] = False
for i in range(len(prime)):
    if prime[i]:
        primes.append(i)

for i in range(int(input())):
    n = int(input())
    for j in range(n//2, 1, -1):
        if j in primes and n-j in primes:
            print(f"{j} {n-j}")
            break
