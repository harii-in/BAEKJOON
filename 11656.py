S = input()
S_list = list()

for _ in S:
    S_list.append(S)
    S = S[1:]

S_list.sort()
for i in S_list:
    print(i)