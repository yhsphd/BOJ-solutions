import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())  # 노드, 간선, 시작노드
adj = [[] for _ in range(N + 1)]  # 인접 리스트 구현

for i in range(M):
    edge = list(map(int, input().split()))
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])

# print(adj)

# 정점 번호가 작은 것을 먼저 방문
for i in range(len(adj)):
    adj[i] = sorted(adj[i])

def DFS(curr, visit=[]):
    ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
    visit.append(curr)

    for node in adj[curr]:
        if node not in visit:
            DFS(node, visit)
    return visit


def BFS(start):
    # 초기화
    q = deque()
    q.append(start)
    visit = [False] * (N + 1)
    visit[start] = True
    adjBFS = []

    for i in range(N + 1):
        adjBFS.append(sorted(adj[i]))

    route = [start]

    # BFS
    while q:
        """
        print(visit)
        print(q)
        """
        curr = q.popleft()  # 먼저 들어온 정점부터 탐색; FIFO
        for nextNode in adj[curr]:
            if visit[nextNode]:
                continue  # 이미 방문한 노드는 패스
            route.append(nextNode)
            q.append(nextNode)
            visit[nextNode] = True

    return route


print(" ".join(map(str, DFS(V))))
print(" ".join(map(str, BFS(V))))
