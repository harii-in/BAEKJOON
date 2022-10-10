import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    queue = deque(arr)
    flag = 0

    if n == 0:
        queue = []
    
    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    
    else:
        if flag % 2 == 0:
                print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")