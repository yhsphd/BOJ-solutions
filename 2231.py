def gen(num):
    return num + sum(map(int, str(num)))


N = int(input())
key = 1

while True:
    if key > N:
        key = 0
        break
    if gen(key) == N:
        break
    key += 1

print(key)
