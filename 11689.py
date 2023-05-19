import sys, math
input = sys.stdin.readline

n = int(input())
result = n

for p in range(2, int(math.sqrt(n))+1):
    # 소인수인지 판별
    if n % p  == 0:
        result -= result / p
        # n이 p의 제곱으로 이루어져 있거나 p의 배수인 경우를 제외하기 위해
        while n % p == 0:
            n /= p

# 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
# 마지막 소인수
if n > 1:
    result -= result / n

print(int(result))