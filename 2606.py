n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(v):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
def DFS(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            DFS(i)

DFS(1)
print(sum(visited)-1)