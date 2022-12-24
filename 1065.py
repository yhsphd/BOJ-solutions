count = 0


def checkHansu(num: int):
    num = list(map(int, str(num)))
    if len(num) == 1:
        return True
    diff = num[1]-num[0]
    for i in range(len(num)-1):
        if num[i+1]-num[i] != diff:
            return False
    return True


for i in range(int(input())):
    if checkHansu(i+1):
        count += 1

print(count)
