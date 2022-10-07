N = int(input())
ans = dict()
for _ in range(N):
    book = input()
    if book not in ans:
        ans[book] = 1
    else:
        ans[book] = ans[book] + 1

result = list()
num = max(ans.values())

for i in ans:
    if num == ans[i]:
        result.append(i)

result.sort()
print(result[0])