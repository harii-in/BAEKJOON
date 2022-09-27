N = int(input())

for i in range(1, N+1):
    tmp = sum(map(int, str(i)))
    tmp += i

    if tmp == N:
        print(i)
        break
    if i == N:
        print(0)