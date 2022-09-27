import sys

input = sys.stdin.readline
N = int(input())
stick = [int(input()) for _ in range(N)]

last = stick.pop()
cnt = 1

for i in range(1, N):
    tmp = stick.pop()

    if tmp > last:
        cnt += 1
        last = tmp

print(cnt)