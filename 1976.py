import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
city = [[0 for j in range(N+1)] for i in range(N+1)]
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

# insert(0, 0)을 하는 이유
# 1. city[i]의 인덱스를 1부터 시작하려고
# 2. city[i]의 인덱스와 route[i]의 인덱스를 맞추려고

# insert(0, 0)을 하지 않으면
# city[i]의 인덱스는 0부터 시작하고
# route[i]의 인덱스는 1부터 시작함
# 그럼 city[i]의 인덱스와 route[i]의 인덱스가 맞지 않음

for i in range(1, N+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)

route = list(map(int, input().split()))
route.insert(0, 0)

for i in range(1, N+1):
    for j in range(1, N+1):
        if city[i][j] == 1:
            union(i, j)

# route[1]의 부모를 찾아서 start에 저장함
start = find(route[1])

for i in range(2, len(route)):
    if parent[route[i]] != start:
        print("NO")
        break
else:
    print("YES")
