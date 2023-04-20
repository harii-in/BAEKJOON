import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = list([] for _ in range(N+1))
visited = [False] * N

def DFS(v, depth):
    if depth == 4:
        print(1)
        exit()
    
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[v] = False


for _ in range(M):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

for i in range(N):
    DFS(i, 0)

print(0)