N = int(input())
Mat = list(map(int, input().split()))
Mat.sort()

visit = [False] * N
cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        if Mat[i] < Mat[j] and not visit[j]:
            visit[j] = True
            break

for i in visit:
    if not i: cnt+=1

print (cnt)