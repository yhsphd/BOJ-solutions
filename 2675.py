for i in range(int(input())):
    inputstr = input()
    rep = int(inputstr.split(" ")[0])
    str = inputstr.split(" ", 1)[1]
    for j in range(len(str)):
        print(str[j]*rep, end="")
    print()
