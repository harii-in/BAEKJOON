N, M = map(int, input().split())

org = []
for _ in range(N):
    org.append(input())

cnt = []
for i in range(N-7):
    for j in range(M-7):
        W = 0   # 맨 위 왼쪽이 W인 경우
        B = 0   # 맨 위 왼쪽이 B인 경우

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if org[x][y] != 'W':
                        W += 1
                    else:
                        B += 1
                else:
                    if org[x][y] != 'B':
                        W += 1
                    else:
                        B += 1
        print(W, B)
        cnt.append(W)
        cnt.append(B)

print(min(cnt))