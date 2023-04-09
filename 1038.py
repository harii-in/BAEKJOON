import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
MAX = 9876543210 # 10

seq = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        tmp = ''.join(list(map(str, reversed(list(j)))))
        seq.append(int(tmp))

seq.sort()
if N >= len(seq):
    print(-1)
else:
    print(seq[N])