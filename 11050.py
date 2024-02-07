def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


N, K = map(int, input().split())
print(factorial(N) // factorial(K) // factorial(N - K))
