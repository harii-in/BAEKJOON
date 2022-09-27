import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []
queue = deque([])

for i in range(N):
    tomato.append(list(map(int, input().split())))

    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < N and 0 <= b < M and tomato[a][b] == 0:
                queue.append([a, b])
                tomato[a][b] = tomato[x][y] + 1

bfs()
ans = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans - 1)