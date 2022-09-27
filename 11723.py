import sys
input = sys.stdin.readline

empty_set = set()

def add(X):
    empty_set.add(X)
def remove(X):
    empty_set.discard(X)
def check(X):
    if X in empty_set:
        print(1)
    else:
        print(0)
def toggle(X):
    if X in empty_set:
        empty_set.discard(X)
    else:
        empty_set.add(X)
def all():
    global empty_set
    empty_set = {i for i in range(1, 21)}
def empty():
    empty_set.clear()

M = int(input())
for _ in range(M):
    tmp = input().split()
    if tmp[0] == 'add':
        add(int(tmp[1]))
    elif tmp[0] == 'remove':
        remove(int(tmp[1]))
    elif tmp[0] == 'check':
        check(int(tmp[1]))
    elif tmp[0] == 'toggle':
        toggle(int(tmp[1]))
    elif tmp[0] == 'all':
        all()
    elif tmp[0] == 'empty':
        empty()