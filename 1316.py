def checkgroup(string: str):
    string = list(string)
    newlst = [string[0]]
    for i in range(len(string)):
        if newlst[-1] != string[i]:
            newlst.append(string[i])
    return len(newlst) == len(set(newlst))


count = 0
for i in range(int(input())):
    if checkgroup(input()):
        count += 1

print(count)
