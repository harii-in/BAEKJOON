N = input()

cnt = [0 for i in range(10)]

for j in N:
    tmp = int(j)
    if tmp == 9:
        tmp = 6
    cnt[tmp] += 1

cnt[6] = (cnt[6] + 1) // 2
print(max(cnt))