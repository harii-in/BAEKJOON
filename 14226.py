import sys
input = sys.stdin.readline
from collections import deque

S = int(input())
queue = deque()
# (s, c) -> s: 현재 이모티콘 개수, c: 클립에 있는 이모티콘 개수
queue.append((1, 0))

visited = dict()
visited[(1, 0)] = 0

while queue:
    s, c = queue.popleft()

    # 걸린 시간 출력
    if s == S:
        print(visited[(s, c)])
        break
    
    # 1. 화면에 있는 이모티콘 모두 복사
    if (s, s) not in visited.keys():
        visited[(s, s)] = visited[(s, c)] + 1
        queue.append((s, s))
    # 2. 클립보드에 있는 모든 이모티콘 화면에 복사
    if (s+c, c) not in visited.keys():
        visited[(s+c, c)] = visited[(s, c)] + 1
        queue.append((s+c, c))
    # 3. 화면에 있는 이모티콘 중 하나 삭제
    if (s-1, c) not in visited.keys():
        visited[(s-1, c)] = visited[(s, c)] + 1
        queue.append((s-1, c))