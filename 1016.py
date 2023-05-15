import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
index = m-n+1
check = [False] * index

for i in range(2, int(math.sqrt(m))+1):
    pow = i*i
    start = int(n / pow)
    if n % pow != 0:
        start += 1
    for j in range(start, int(m / pow)+1):
        check[(j*pow)-n] = True

cnt = 0

for i in range(index):
    if not check[i]:
        cnt += 1

print(cnt)