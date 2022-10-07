N, M = map(int, input().split())
level = list(map(int, input().split()))

sum = 0
id = 100001
for i in range(M):
    tmp = list(input().split())
    tmp_sum = 0
    for j in range(1, N+1):
        if tmp[j] == 'O':
            tmp_sum += int(level[j-1])

    if sum < tmp_sum:
        sum = tmp_sum
        id = int(tmp[0])
    elif sum == tmp_sum:
        id = min(id, int(tmp[0]))

print(id, sum)