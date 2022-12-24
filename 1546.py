input()
scores = list(map(int, input().split(" ")))
print((sum(scores)/len(scores))*100/max(scores))
