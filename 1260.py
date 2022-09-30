import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def DFS(start):
    print(start, end=' ')
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
            visited[i] = True
 
def BFS(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        tmp = queue.popleft()
        print(tmp,end = ' ')

        for i in graph[tmp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

DFS(V)
visited=[False] * (N+1)
print()
BFS(V)