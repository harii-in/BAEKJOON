import sys
input = sys.stdin.readline  # 개행문자까지 저장하므로 rstrip()이 필요

N, M = map(int, input().split())

pockmon = {}

for i in range(1, N+1):
    tmp = input().rstrip()
    pockmon[i] = tmp
    pockmon[tmp] = i


for _ in range(M):
    tmp = input().rstrip()
    if tmp.isalpha() == True:
        print(pockmon[tmp])
    else:
        print(pockmon[int(tmp)])
