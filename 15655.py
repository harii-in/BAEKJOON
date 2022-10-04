N, M = map(int, input().split())
num = list(map(int, input().split()))
s = []

def DFS(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N):
        if num[i] not in s:
            s.append(num[i])
            DFS(i+1)
            s.pop()

num.sort()
DFS(0)