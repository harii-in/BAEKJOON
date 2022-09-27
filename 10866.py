import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

def push_front(X):
    queue.appendleft(X)
def push_back(X):
    queue.append(X)
def pop_front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())
def pop_back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop())
def size():
    print(len(queue))
def empty():
    if len(queue) == 0:
            print(1)
    else:
        print(0)
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


for _ in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push_front':
        push_front(tmp[1])
    elif tmp[0] == 'push_back':
        push_back(tmp[1])
    elif tmp[0] == 'pop_front':
        pop_front()
    elif tmp[0] == 'pop_back':
        pop_back()
    elif tmp[0] == 'size':
        size()
    elif tmp[0] == 'empty':
        empty()
    elif tmp[0] == 'front':
        front()
    elif tmp[0] == 'back':
        back()