num = input().split(" ")
num = [int(x) for x in num]

if (num[0] < num[1]):
    print("<")
elif (num[0] > num[1]):
    print(">")
else:
    print("==")
