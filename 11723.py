"""
    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다.
"""

import sys

input = sys.stdin.readline

s = [False for _ in range(21)]

for _ in range(int(input())):
    comm = input().split()
    if(len(comm) == 2):
        arg = int(comm[1])
    if(comm[0] == "add"):
        s[arg] = True
    elif(comm[0] == "remove"):
        s[arg] = False
    elif(comm[0] == "check"):
        print(int(s[arg]))
    elif(comm[0] == "toggle"):
        s[arg] = not s[arg]
    elif(comm[0] == "all"):
        s = [True for _ in range(21)]
    elif(comm[0] == "empty"):
        s = [False for _ in range(21)]
    