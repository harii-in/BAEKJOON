import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    bust = list(map(int, input().split()))
else:
    bust = []

cnt = abs(100 - N)
for num in range(1000001):
    for j in str(num):
        if int(j) in bust:
            break
    else:
        cnt = min(cnt, (len(str(num)) + abs(num - N)))
print(cnt)