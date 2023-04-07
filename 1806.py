import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

sum = 0
left, right = 0, 0
min_length = sys.maxsize

while True:
    if sum >= S:
        min_length = min(min_length, right - left)
        sum -= num_list[left]
        left += 1
    elif right == N:
        break
    else:
        sum += num_list[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)