import math
from operator import contains

N = int(input())
tmp = math.factorial(N)

cnt = 0

for i in reversed(str(tmp)):
    if i != '0':
        break

    if i == '0':
        cnt += 1
print(cnt)