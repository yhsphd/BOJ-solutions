import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
heights = []
for _ in range(N):
    heights.extend(map(int, input().split()))

minimum, maximum = min(heights), max(heights)

timereqmin = -1
ansheight = 0

for height in range(minimum, maximum + 1).__reversed__():
    diff = [x - height for x in heights]
    delete, add = 0, 0
    for n in diff:
        if n > 0:
            delete += n
        else:
            add -= n

    if delete + B - add >= 0:  # possible
        timereq = 2 * delete + add
        if timereqmin > timereq or timereqmin == -1:
            timereqmin = timereq
            ansheight = height

print(timereqmin, ansheight)
