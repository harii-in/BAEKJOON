import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().rstrip())
med = [list(input().strip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

not_blind = 0
blind = 0

#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    visited[x][y] = True
    current_color = med[x][y]

    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == False:
                if med[nx][ny] == current_color:
                    DFS(nx, ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            DFS(i, j)
            not_blind += 1

for i in range(N):
    for j in range(N):
        if med[i][j] == 'G':
            med[i][j] = 'R'
            
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            DFS(i, j)
            blind += 1

print(not_blind, blind)