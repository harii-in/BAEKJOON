import sys
from collections import deque

#input = sys.stdin.readline

N = int(input())
max_num = 0
max_list = []

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] > max_num:
            max_num = graph[i][j]

#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y, target):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > target and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for k in range(max_num):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                BFS(i, j, k)
                cnt += 1
    max_list.append(cnt)

print(max(max_list))