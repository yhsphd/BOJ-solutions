def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a


numbers = list(map(int, input().split()))
gcd = Euclidean(numbers[0], numbers[1])
print(gcd)
print(numbers[0] * numbers[1] // gcd)
