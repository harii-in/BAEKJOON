import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
queue = deque([])

for k in range(H):
    tmp = []
    for i in range(N):
        tmp.append(list(map(int, input().split())))
        for j in range(M):
            if tmp[i][j] == 1:
                queue.append([k, i, j])
    tomato.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]

            if 0 <= a < H and 0 <= b < N and 0 <= c < M and tomato[a][b][c] == 0:
                queue.append([a, b, c])
                tomato[a][b][c] = tomato[x][y][z] + 1

bfs()
ans = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans - 1)