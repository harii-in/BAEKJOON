import sys
input = sys.stdin.readline

N = int(input())
meet = [list(map(int, input().split())) for _ in range(N)]

meet.sort(key=lambda x: (x[1], x[0]))

maxCnt = 0
curEndTime= 0

for start, end in meet:
    if curEndTime <= start:
        curEndTime = end
        maxCnt += 1

print(maxCnt)