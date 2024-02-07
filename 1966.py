import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    documents = list(range(N))

    count = 0
    # print(documents)
    # print(priorities)

    priority = max(priorities)
    while len(documents):
        if priorities[0] != priority:
            # move to last
            documents.append(documents.pop(0))
            priorities.append(priorities.pop(0))
        else:  # priority document; print
            count += 1
            priorities.pop(0)
            if documents.pop(0) == M:
                break  # no need to proceed
            priority = max(priorities)  # refresh priority when an item is cleared

    print(count)
