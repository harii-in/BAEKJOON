import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
queue = deque()

def BFS(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if not visited[i]:
                visited[i] = visited[tmp] + 1
                queue.append(i)
    return sum(visited)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

kevin = []
for i in range(1, N+1):
    visited = [0] * (N+1)
    kevin.append(BFS(i))

print(kevin.index(min(kevin)) + 1)