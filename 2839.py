N = int(input())
bs = N // 5
while True:
    if bs < 0:
        print(-1)
        break
    elif (N - 5 * bs) % 3 == 0:
        print(bs + (N - 5 * bs) // 3)
        break
    else:
        bs -= 1
