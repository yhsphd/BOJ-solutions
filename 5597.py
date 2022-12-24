students = [False]*30
for i in range(28):
    students[int(input())-1] = True

ans = []
for i in range(30):
    if not students[i]:
        ans.append(i+1)

print("\n".join(map(str, sorted(ans))))
