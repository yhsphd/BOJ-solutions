counts = input().split(" ")
counts = [int(x) for x in counts]
ans = [1 - counts[0], 1 - counts[1], 2 - counts[2],
       2 - counts[3], 2 - counts[4], 8 - counts[5]]
ans = [str(x) for x in ans]
print(" ".join(ans))
