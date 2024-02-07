import sys

input = sys.stdin.readline

N = int(input())
seq = []

for _ in range(N):
    seq.append(int(input()))

# print(seq)

pool = list(range(1, N + 1))
stack = []
inst = []

last = 0

flag = True
seek = 0
while True:
    if len(stack) > 0 and stack[-1] == seq[seek]:  # match success
        inst.append("-")
        last = stack.pop()
        seek += 1
    elif last < seq[seek]:
        if len(pool) == 0:  # failed; else try pushing more
            flag = False
            break
        inst.append("+")
        stack.append(pool.pop(0))
    elif last > seq[seek]:
        inst.append("-")
        last = stack.pop()
        if last != seq[seek]:  # failed; else match success
            flag = False
            break
        seek += 1

    # print(pool)
    # print(stack)
    # print(inst)

    if seek == len(seq):  # complete
        break

if flag:
    print("\n".join(inst))
else:
    print("NO")
