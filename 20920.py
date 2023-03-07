import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word = {}
for _ in range(N):
    tmp = input().rstrip()

    if len(tmp) < M:
        continue
    else:
        if word.get(tmp):
            word[tmp] += 1
        else:
            word[tmp] = 1

word = sorted(word.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word:
    print(i[0])