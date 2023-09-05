N, K = map(int, input().split())
m = N //2
if K == 0:
    print('B'*N)
elif m*(N-m) < K:
    print(-1)
else:
    a = 0   # A의 개수
    b = N   # B의 개수
    while a*b < K and b > 0:
        a += 1
        b -= 1
    b_back = K - (a-1)*b
    print('A'*(a-1) + 'B'*(b-b_back) + 'A' + 'B'*b_back)