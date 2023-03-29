from collections import deque

queue = deque(range(int(input())+1))
queue.popleft()

if len(queue) == 1:
    print(queue[0])
else:
    while True:
        queue.popleft()
        if len(queue) == 1:
            break
        queue.append(queue[0])
        queue.popleft()
    print(queue[0])
