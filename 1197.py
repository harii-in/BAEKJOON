import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
total_cost = 0

# 부모테이블 초기화
parent = list(range(V + 1))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()

for i in range(E):
    cost, a, b = edges[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost

print(total_cost)