import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def BFS(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        if abs(x - rock_x) + abs(y - rock_y) <= 1000:
            print("happy")
            return
        
        for i in range(n):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <=1000:
                    queue.append((nx, ny))
                    visited[i] = True
    print("sad")
    return


for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    conv = [list(map(int, input().split())) for _ in range(n)]
    rock_x, rock_y = map(int, input().split())

    visited = [False] * (n+1)

    BFS(home_x, home_y)