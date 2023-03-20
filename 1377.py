import sys
input = sys.stdin.readline

N = int(input())
num = []
for i in range(N):
    num.append((int(input()), i))

MAX = 0
sorted_num = sorted(num)

for i in range(N):
    tmp = sorted_num[i][1] - i
    if MAX < tmp:
        MAX = tmp
print(MAX + 1)