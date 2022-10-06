N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
s = []

def DFS(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    overlap = 0
    for i in range(start, N):
        if overlap != num[i]:
            s.append(num[i])
            overlap = num[i]
            DFS(i)
            s.pop()

DFS(0)