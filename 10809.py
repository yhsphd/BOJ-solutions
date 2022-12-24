string = input()
ans = ""

for i in range(97, 123):
    found = False
    for j in range(len(string)):
        if ord(string[j]) == i:
            found = True
            ans += f"{j} "
            break
    if found:
        continue
    else:
        ans += "-1 "

print(ans)
