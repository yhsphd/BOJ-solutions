while True:
    flag = True
    num = input()
    if num == "0":
        break

    for i in range(len(num) // 2):
        if num[i] != num[-1 - i]:
            print("no")
            flag = False
            break

    if flag:
        print("yes")
