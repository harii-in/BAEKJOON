import sys

N = int(input())
bulb = list(map(int, input()))
goal = list(map(int, input()))

def reverse(bulb):
    cnt = 0
    for i in range(1, N):
        if bulb[i - 1] != goal[i - 1]:
            cnt += 1
            for j in range(i - 1, i + 2):
                if j < N:
                    bulb[j] = 1 - bulb[j]
    if bulb == goal:
        return cnt
    else:
        return sys.maxsize

# 1번 스위치를 누르지 않는 경우
ans = reverse(bulb[:])

# 1번 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
ans = min(ans, 1 + reverse(bulb[:]))

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)