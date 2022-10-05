N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
visited = [False] * N
s = []

def DFS(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != num[i]:
            visited[i] = True
            s.append(num[i])
            overlap = num[i]
            DFS(i+1)
            visited[i] = False
            s.pop()

DFS(0)