import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque()

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(BFS(0, 0))