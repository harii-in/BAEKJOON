N, M = list(map(int,input().split()))
 
s = []
 
def DFS(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1):
        s.append(i)
        DFS(i+1)
        s.pop()
 
DFS(1)