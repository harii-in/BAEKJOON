N, M = map(int, input().split())
num = list(map(int, input().split()))
s = []

def DFS():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in num:
        s.append(i)
        DFS()
        s.pop()

num.sort()
DFS()