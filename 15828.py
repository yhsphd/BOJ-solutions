import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
packets = deque([])

while True:
    num = int(sys.stdin.readline().rstrip())
    if num == -1:
        break
    elif num == 0:
        packets.popleft()
    elif len(packets) < N:
        packets.append(num)

if len(packets) == 0:
    print("empty")
else:
    print(" ".join(map(str, packets)))
