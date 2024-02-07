while True:
    case = list(map(int, input().strip().split()))
    if not sum(case):
        break
    squared = [n ** 2 for n in case]
    if sum(squared) == 2 * max(squared):
        print("right")
    else:
        print("wrong")
