import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
ans = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if not visited[i]:
                visited[i] = True
                ans[i] += 1
                queue.append(i)

# 모든 노드에서 BFS 실행
for i in range(1, N+1):
    visited = [False] * (N+1)
    BFS(i)

max_cnt = max(ans)
for i in range(1, N+1):
    if max_cnt == ans[i]:
        print(i, end=' ')