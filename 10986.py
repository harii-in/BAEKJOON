import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

sum = 0
remainder = [0] * M

for i in range(N):
    sum += num[i]
    remainder[sum%M] +=1

result = remainder[0]
for i in remainder:
    result += i*(i-1) // 2

print(result)