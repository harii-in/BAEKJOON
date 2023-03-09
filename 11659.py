import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))

sum = [0]
total = 0
for i in num:
    total += i
    sum.append(total) 

for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])