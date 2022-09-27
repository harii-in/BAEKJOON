import sys

N = int(sys.stdin.readline())
stack = []

def push(X):
    stack.append(X)
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
            print(1)
    else:
        print(0)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

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
    elif tmp[0] == 'top':
        top()