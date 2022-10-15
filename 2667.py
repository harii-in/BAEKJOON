import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
queue = deque()

#상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    queue.append((x, y))
    graph[x][y] = -1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = -1
                cnt += 1
    return cnt

house_cnt = list(BFS(i, j) for i in range(N) for j in range(N) if graph[i][j] == 1)
house_cnt.sort()
print(house_cnt)

total = len(house_cnt)
print(total)
for i in range(total):
    print(house_cnt[i])