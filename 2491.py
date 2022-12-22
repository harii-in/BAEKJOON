N = int(input())
N_list = list(map(int, input().split()))

min_cnt = 1
max_cnt = 1
max_len = 1

prev = N_list[0]
for i in N_list[1:]:
    if(prev <= i):
        max_cnt += 1
    else:
        max_cnt = 1
    
    if(prev >= i):
        min_cnt += 1
    else:
        min_cnt = 1
    
    prev = i
    max_len = max(max_len, min_cnt, max_cnt)

print(max_len)