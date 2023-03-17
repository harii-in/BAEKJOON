import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
num = list(map(int, input().split()))

queue = deque()
for i in range(N):
    if queue and queue[0][0] <= i-L:
        queue.popleft()

    while queue and queue[-1][1] > num[i]:
        queue.pop()
    
    queue.append((i, num[i]))
    print(queue[0][1], end = ' ')