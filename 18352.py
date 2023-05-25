import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# BFS
visited = [-1] * (N+1)
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1

    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            # 현재 노드의 연결 노드 증 미 방문 노드라면
            if visited[i] == -1:
                visited[i] = visited[tmp] + 1
                queue.append(i) 

BFS(X)
for i in range(N+1):
    if visited[i] == K:
        ans.append(i)

if not ans:
    print(-1)
else:
    print(*ans, sep='\n')