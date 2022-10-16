import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [False] * (F+1)

def BFS():
    queue = deque()
    queue.append ((S, 0))
    visited[S] = True

    while queue:
        tmp, cnt = queue.popleft()
        if tmp == G:
            return cnt
        for i in (tmp + U, tmp - D):
            if 1 <= i <= F and not visited[i]:
                visited[i] = True
                queue.append((i, cnt+1))
    return 'use the stairs'

print(BFS())