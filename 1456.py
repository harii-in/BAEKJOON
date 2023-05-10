import sys, math
input = sys.stdin.readline

A, B = map(int, input().split())
point = int(math.sqrt(B))

# 제곱근까지만 탐색하여 시간 아낌
prime = [True] * (point + 1)
# 모든 수를 소수라고 가정
prime[1] = False

# 소수 판별
for i in range(2, point + 1):
    if prime[i]:
        if i*i > point:
            break
        for j in range(int(math.pow(i, 2)), point + 1, i):
            prime[j] = False

# 거의 소수 구하기
cnt = 0
for i in range(1, len(prime)):
    if prime[i]:
        res = int(math.pow(i, 2))
        while True:
            if res < A:
                res *= i
                continue
            if res > B:
                break
            res *= i
            cnt += 1
print(cnt)