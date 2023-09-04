N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

cnt = 0

# 행렬 A를 행렬 B로 바꾸는 함수
def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]

if (N < 3 or M < 3) and A != B:
    print(-1)
    exit()
else:
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                cnt += 1
                reverse(i, j)

if A != B:
    print(-1)
else:
    print(cnt)