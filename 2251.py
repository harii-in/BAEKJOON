from collections import deque
import sys
input = sys.stdin.readline

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))

def BFS():
    while queue:
            
        # x: A물통의 물의 양, y: B물통의 물의 양,z: C물통의 물의 양
        x, y = queue.popleft()
        z = C - x - y

        # A물통이 비어있는 경우 C 물통에 남아있는 물의 양 추가
        if x == 0:
            ans.append(z)

        # x -> y
        water = min(x, B-y)
        pour(x-water, y+water)
        # x -> z
        water = min(x, C-z)
        pour(x-water, y)

        # y -> x
        water = min(y, A-x)
        pour(x+water, y-water)
        # y -> z
        water = min(y, C-z)
        pour(x, y-water)

        # z -> x
        water = min(z, A-x)
        pour(x+water, y)
        # z -> y
        water = min(z, B-y)
        pour(x, y+water)

A, B, C = map(int, input().split())

# 경우의 수를 답을 큐
queue = deque()
queue.append((0, 0))

# 방문여부 - 초기에 A, B, C = 0, 0, C이므로 (0, 0)은 방문한 것으로 처리
visited = [[False] * (B+1) for _ in range(A+1)]
visited[0][0] = True

ans = []    # 답

BFS()

ans.sort()
print(*ans)