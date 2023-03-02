N, K = map(int, input().split())
back = {0:0}

for _ in range(N):
    cur_w, cur_v = map(int, input().split())
    temp = {}

    for w, v in back.items():
        if cur_w + w <= K and cur_v + v > back.get(cur_w + w, 0):
            temp[cur_w + w] = cur_v + v
    back.update(temp)
print(max(back.values()))