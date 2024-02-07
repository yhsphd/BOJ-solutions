import re
import sys

input = sys.stdin.readline

while True:
    txt = re.sub("[\r\n]", "", input())
    if txt == ".":
        break
    txt = re.sub("[^()\\[\\]]", "", txt)
    # print(txt)
    stack = []
    valid = True
    for char in txt:
        # print(stack)
        if char == "(" or char == "[":
            stack.append(char)
        else:  # ) or ]
            if len(stack) == 0:
                valid = False
                break
            cmp = stack.pop()
            if not ((char == ")" and cmp == "(") or (char == "]" and cmp == "[")):
                valid = False
                break
    if len(stack) != 0:
        valid = False

    print("yes" if valid else "no")
