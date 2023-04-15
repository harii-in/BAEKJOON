import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())

maps = list(list(input()) for _ in range(N))
visited = list([float('inf')] * M for _ in range(N))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1

queue = deque()
queue.append((x1, y1))
visited[x1][y1] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        nk = 1
        
        while nk <= K and 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != '#' and visited[nx][ny] > visited[x][y]:
            if visited[nx][ny] == float('inf'):
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            nk += 1

if visited[x2][y2] == float('inf'):
    print(-1)
else:
    print(visited[x2][y2])