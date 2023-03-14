import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

for k in range(N):
    target = num[k]
    i, j = 0, N-1

    while i < j:
        if num[i] + num [j] == target:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif num[i] + num [j] < target:
            i += 1
        else:
            j -= 1
print(cnt)