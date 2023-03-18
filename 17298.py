import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
result = [-1] * N
stack = []

for i in range(N):
    while stack and num[stack[-1]] < num[i]:
        result[stack.pop()] = num[i]
    stack.append(i)

print(*result)