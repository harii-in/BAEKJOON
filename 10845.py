import sys

N = int(sys.stdin.readline())
queue = []

def push(X):
    queue.append(X)
def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))
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
    if tmp[0] == 'push':
        push(tmp[1])
    elif tmp[0] == 'pop':
        pop()
    elif tmp[0] == 'size':
        size()
    elif tmp[0] == 'empty':
        empty()
    elif tmp[0] == 'front':
        front()
    elif tmp[0] == 'back':
        back()
