cut = int(input().split()[1])
scores = sorted(list(map(int, input().split())))

print(scores[-cut])
