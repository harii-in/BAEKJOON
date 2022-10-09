N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
coin.sort(reverse = True)
cnt = 0

for i in coin:
    cnt += (K // i)
    K %= i

print(cnt)