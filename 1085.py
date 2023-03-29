xywh = list(map(int, input().split()))
d = [xywh[0], xywh[1], xywh[2] - xywh[0], xywh[3] - xywh[1]]
print(sorted(d)[0])
