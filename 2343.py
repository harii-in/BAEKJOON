import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lesson = list(map(int, input().split()))

start = max(lesson)
end = sum(lesson)

# 블루레이의 개수가 많으면 블루레이 크기를 늘리고,
#  블루레이 개수가 적으면 블루레이 크기를 줄여간다
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    sum = 0

    for i in range(N):
        if sum + lesson[i] > mid:
            cnt += 1
            sum = 0
        sum += lesson[i]
    if sum:
        cnt += 1
        
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)