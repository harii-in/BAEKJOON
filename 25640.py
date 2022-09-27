import sys
input = sys.stdin.readline

jinho = input()
N = int(input())
cnt = 0

for i in range(N):
    if jinho == input():
        cnt += 1

print(cnt)