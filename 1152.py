string = input()
if string == " ":
    print(0)
else:
    print(len(string.rstrip().lstrip().split(" ")))
