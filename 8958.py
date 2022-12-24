for i in range(int(input())):
    streaks = list(filter(None, input().split("X")))
    points = 0
    for streak in streaks:
        n = len(streak)
        points += n * (n+1) // 2
    print(points)
