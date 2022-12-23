N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
for i in range(N):
    tmp = A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
    S += tmp
print(S)