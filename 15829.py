M = 1234567891
r = 31

L = int(input())
s = input()
ans = 0

for i in range(L):
    ans += (ord(s[i])-96) * (r ** i)

print(ans % M)