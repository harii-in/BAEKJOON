S = input()
ans = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        tmp = S[i : j+1]
        ans.add(tmp)
print(len(ans))