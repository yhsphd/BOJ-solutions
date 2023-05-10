import sys
from collections import deque

queue = deque([])

rep = int(sys.stdin.readline().rstrip())
for i in range(rep):
    command = sys.stdin.readline().rstrip()
    if command.startswith("push"):
        num = int(command.split(" ")[1])
        queue.append(num)
    elif command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        print(1 if len(queue) == 0 else 0)
    elif command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    # print(queue)
