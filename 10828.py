import sys

stack = []

rep = int(sys.stdin.readline().rstrip())
for i in range(rep):
    command = sys.stdin.readline().rstrip()
    if command.startswith("push"):
        stack.append(int(command.split(" ")[1]))
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    # print(queue)
