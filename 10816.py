N = int(input())
card = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))
cnt = {}

for x in card:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1
    
for i in check:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")