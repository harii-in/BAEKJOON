import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

def DFS(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)