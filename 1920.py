input()
pool = set(map(int, input().split()))
input()
comp = map(int, input().split())
for num in comp:
    print(int(num in pool))
