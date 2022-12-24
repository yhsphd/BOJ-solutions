string = input()
tot=0

for i in range(len(string)):
    if string[i] in "ABC":
        tot+=3
    elif string[i] in "DEF":
        tot+=4
    elif string[i] in "GHI":
        tot+=5
    elif string[i] in "JKL":
        tot+=6
    elif string[i] in "MNO":
        tot+=7
    elif string[i] in "PQRS":
        tot+=8
    elif string[i] in "TUV":
        tot+=9
    elif string[i] in "WXYZ":
        tot+=10

print(tot)