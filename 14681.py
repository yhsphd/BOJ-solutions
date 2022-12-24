point = [input(), input()]
point = [int(x) for x in point]

if (point[0] > 0):
    if (point[1] > 0):
        print(1)
    elif (point[1] < 0):
        print(4)
elif (point[0] < 0):
    if (point[1] > 0):
        print(2)
    elif (point[1] < 0):
        print(3)
