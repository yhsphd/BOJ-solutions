fib = [0, 1]

for i in range(2, 21):
    fib.append(fib[i - 1] + fib[i - 2])

print(fib[int(input())])
