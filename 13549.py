import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

# [지점 i에 도달하는데 걸린 시간, 경우의 수]
visited = list(-1 for _ in range(100001))

# BFS 메서드 정의
def BFS(n):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([n])
    # 현재 노드를 방문 처리
    visited[n] = 0
    
    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()

        # 동생의 위치에 도착할 시 리턴
        if v == K:
            return visited[v]

        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in [v-1, v+1, v*2]:
            # 이동하는 곳이 범위 내에 있고 이동하지 않았다면 이동
            if 0 <= i <= 100000 and visited[i] == -1:
                # 0초 후: 순간이동
                if i == v*2:
                    visited[i] = visited[v]
                    # 우선 순위가 높기에 먼저 탐색
                    queue.appendleft(i)
                # 1초 후: 걸어서 이동
                else:
                    visited[i] = visited[v] + 1
                    queue.append(i)

# 정의한 BFS 메서드 호출(노드 1을 탐색 시작 노드로 설정)
print(BFS(N))