N = int(input())
P = list(map(int, input().split()))

P.sort()
time = 0

for i in range(1, N+1):
    time += sum(P[0:i])     #리스트의 0부터 i-1까지 값의 합
print(time)