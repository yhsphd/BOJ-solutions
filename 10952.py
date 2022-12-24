while True:
    inputstr = input()
    if inputstr == "0 0":
        break
    num = inputstr.split(" ")
    num = [int(x) for x in num]
    print(num[0] + num[1])
