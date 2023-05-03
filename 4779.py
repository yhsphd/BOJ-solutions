import sys

input = sys.stdin.readline


def Cantoring(string):
    if len(string) == 1:  # 종료조건
        return string
    # 3등분하여 재귀호출
    nextDepth = Cantoring(string[0:len(string) // 3])
    # 3등분 중 가운데는 비우고, 좌우대칭이므로 왼쪽 string 재활용
    return nextDepth + (" " * (len(string) // 3)) + nextDepth


while (True):
    try:
        N = int(input())
        print(Cantoring("-" * (3 ** N)))
    except:
        break
