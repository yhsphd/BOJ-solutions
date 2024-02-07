for _ in range(int(input())):
    case = input().strip()
    step = 0
    flag = True
    for char in case:
        if char == "(":
            step += 1
        elif char == ")":
            step -= 1
        if step < 0:
            break
    if step == 0:
        print("YES")
    else:
        print("NO")
