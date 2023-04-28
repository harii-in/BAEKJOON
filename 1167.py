import sys
input = sys.stdin.readline
from collections import deque

# 노드의 개수
v = int(input())
# 트리 리스트
graph = list([] for _ in range(v+1))

# 정점 번호, 거리, 마지막 입력 -1
for _ in range(v):
    data = list(map(int, input().split()))
    # 0번째: 정점번호, 마지막 -1을 제외하고 저장
    for e in range(1, len(data)-2, 2):
        # 연결된 노드와 거리 (정점번호, 거리)
        graph[data[0]].append((data[e], data[e+1]))

def BFS(start):
    visited = [-1] * (v+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    # 거리가 가장 먼 트리의 지름과 정점을 저장하는 배열
    _max = [0, 0]

    while queue:
        # 현재 노드 기준
        tmp = queue.popleft()
        # 현재 기준 노드와 tmp와 연결된 노드 중 거리가 가장 먼 노드 찾기
        for e, w in graph[tmp]:
            # 방문하지 않은 노드 갱신
            if visited[e] ==  -1:
                visited[e] = visited[tmp] + w
                queue.append(e)
                # 현재 노드로부터 거리가 가장 먼 노드의 지름과 정점 갱신
                if _max[0] < visited[e]:
                    _max = visited[e], e
    return _max
                
# 임의의 노드x를 기준으로 가장 먼 노드 y 탐색                
distance, node = BFS(1)
# 노드 y를 기준으로 가장 먼 노드 x를 탐색
distance, node = BFS(node)
# 트리의 지름 노드 y와 노드 z사이의 거리
print(distance)