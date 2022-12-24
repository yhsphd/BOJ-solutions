while True:
    try:
        num = input().split(" ")
        num = [int(x) for x in num]
        print(num[0] + num[1])
    except:
        break
