count = [0]*10
num = 1

for i in range(3):
    num *= int(input())

while num > 0:
    count[num % 10] += 1
    num //= 10

print("\n".join(map(str, count)))
