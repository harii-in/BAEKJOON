import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 10 ** 5
visited = [0] * (MAX + 1)


def BFS():
    queue = deque()
    queue.append(N)

    while queue:
        tmp = queue.popleft()
        if tmp == K:
            print(visited[K])
            break
        for i in (tmp-1, tmp+1, tmp*2):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[tmp] + 1
                queue.append(i)

BFS()