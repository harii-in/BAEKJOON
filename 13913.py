import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

visited = list(0 for _ in range(100001))
prev = list(0 for _ in range(100001))

def path(x):
    arr = []
    temp = x
    for _ in range(visited[x] + 1):
        arr.append(temp)
        temp = prev[temp]
    return arr[::-1]

def BFS(n):
    queue = deque([n])
    
    while queue:
        v = queue.popleft()

        if v == K:
            path(v)
            return visited[v]

        for i in [v-1, v+1, v*2]:
            if 0 <= i <= 100000 and visited[i] == 0:
                    queue.append(i)
                    visited[i] = visited[v] + 1
                    prev[i] = v


print(BFS(N))
print(*path(K))