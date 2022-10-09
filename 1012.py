import sys
sys.setrecursionlimit(10000)

def DFS(x, y):
    #상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if field[ny][nx] == 1:
                field[ny][nx] = -1 #방문했음.
                DFS(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) #가로, 세로, 개수
    field = list([0]*M for _ in range(N))
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    for x in range(M):
        for y in range(N):
            if field[y][x] == 1:
                DFS(x, y)
                cnt += 1

    print(cnt)