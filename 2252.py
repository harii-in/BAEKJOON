import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        tmp = q.popleft()
        result.append(tmp)
        
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(*result, sep=" ")

topology_sort()