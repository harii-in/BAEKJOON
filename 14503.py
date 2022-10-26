import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]

visited[r][c] = 1     # 처음 위치
cnt = 1     # 청소하는 칸의 개수
turn_cnt = 0    # 회전 횟수

#좌, 하, 우, 상 -> 로봇이 반시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 북: 0, 동: 1, 남: 2, 서: 3 -> 좌하우상: 3210
# 로봇 청소기 회전: d -= 1
def turn():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn()
    nx = r + dx[d]
    ny = c + dy[d]

    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
    
        r, c = nx, ny
        turn_cnt = 0
        
        continue    # 회전해서 이동했으니까 밑에는 건너뜀.
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nx = r - dx[d]
        ny = c - dy[d]

        if graph[nx][ny] == 0:
            r, c = nx, ny
        else:
            break
        turn_cnt = 0

print(cnt)