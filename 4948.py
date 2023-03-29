import math

MAX = 123456 * 2 + 1
prime = [True] * MAX
prime[1] = False

for i in range(2, math.floor(math.sqrt(MAX)) + 1):
    if prime[i]:
        for j in range(i * 2, MAX, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(sum(prime[n + 1:n * 2 + 1]))
