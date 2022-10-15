import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
result = -1

def DFS(tmp, cnt):
    global result
    visited[tmp] = True

    if tmp == b:
        result = cnt
        return
        
    for i in graph[tmp]:
        if not visited[i]:
            DFS(i, cnt+1)
    

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(a, 0)
print(result)