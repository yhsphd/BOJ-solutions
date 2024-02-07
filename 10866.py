import sys

input = sys.stdin.readline
deque = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "push_front":
        deque.insert(0, int(command[1]))
    if command[0] == "push_back":
        deque.append(int(command[1]))
    if command[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    if command[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    if command[0] == "size":
        print(len(deque))
    if command[0] == "empty":
        print(int(len(deque) == 0))
    if command[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if command[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
