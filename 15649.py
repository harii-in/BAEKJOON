N, M = list(map(int,input().split()))
 
s = []
 
def DFS():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            DFS()
            s.pop()
 
DFS()