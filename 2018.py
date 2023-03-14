import sys
input = sys.stdin.readline

N = int(input())
start, end = 1, 1
cnt = 1
sum = 1

while end != N:
    if sum == N:
        cnt += 1
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end
print(cnt)


# 이중 for문 - 시간초과
# cnt = 0
# sum = 0
# for i in range(1, N+1):
#     for j in range(i, N+1):
#         sum += j
#         if(sum == N):
#             cnt += 1
#             sum = 0
#             break
#         elif sum > N:
#             sum = 0
#             break
# print(cnt)