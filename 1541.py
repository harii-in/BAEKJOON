import sys
input = sys.stdin.readline

num = list(map(str, input().split("-")))
ans = 0

def mySum(i):
    sum = 0
    tmp = str(i).split("+")
    for i in tmp:
        sum += int(i)
    return sum

for i in range(len(num)):
    tmp = mySum(num[i])
    if i == 0:
        ans += tmp
    else:
        ans -= tmp
print(ans)