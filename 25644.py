N = int(input())
stock = list(map(int, input().split()))

min_ = stock[0]
max_ = 0
result = 0

for i in range(1, N):
    if min_ < stock[i]:
        result = max(result, stock[i]-min_)
    else:
        min_ = stock[i]

print (result)