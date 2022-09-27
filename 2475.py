tmp = list(map(int, input().split()))

ans = 0
for i in tmp:
    ans += i*i

print(ans % 10)