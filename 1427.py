count = [0] * 10

digits = list(map(int, list(input())))

for digit in digits:
    count[digit] += 1

ans = ""
for i in range(10):
    ans = str(i) * count[i] + ans

print(ans)
