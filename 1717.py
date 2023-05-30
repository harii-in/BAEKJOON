import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def isSameParent(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

    # return find(a) == find(b)     # 한 줄로 줄일 수 있음

for i in range(M):
    w, a, b = map(int, input().split())
    if w == 0:
        union(a, b)
    else:
        if isSameParent(a, b):
            print("YES")
        else:
            print("NO")