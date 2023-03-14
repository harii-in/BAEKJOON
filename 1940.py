import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

i, j = 0, N-1
while i < j:
    if num[i] + num[j] < M:
        i += 1
    elif num[i] + num[j] > M:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1
print(cnt)
