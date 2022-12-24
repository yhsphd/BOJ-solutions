string = input()
ans = 0

while len(string) > 0:
    if string.startswith("dz="):
        ans += 1
        string = string[3:]
        continue
    elif string.startswith("c="):
        ans += 1
        string = string[2:]
        continue
    elif string.startswith("c-"):
        ans += 1
        string = string[2:]
        continue
    elif string.startswith("d-"):
        ans += 1
        string = string[2:]
        continue
    elif string.startswith("lj"):
        ans += 1
        string = string[2:]
        continue
    elif string.startswith("nj"):
        ans += 1
        string = string[2:]
        continue
    elif string.startswith("s="):
        ans += 1
        string = string[2:]
        continue
    elif string.startswith("z="):
        ans += 1
        string = string[2:]
        continue
    else:
        ans += 1
        string = string[1:]

print(ans)
