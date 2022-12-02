N, X = map(int, input().split())

# 전체 장 수
burger = [1] * 51
# 패티 수
patty = [1] * 51

for i in range(1, N+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]

def eat(N, X):
    if N == 0:
        return X
    if X == 1:
        return 0
    elif X <= 1 + burger[N-1]:
        return eat(N-1, X-1)
    elif X == 1 + burger[N-1] + 1:      # 중간 패티까지 먹은 경우
        return patty[N-1] + 1
    elif X <= 1 + burger[N-1] + 1 + burger[N-1]:
        return patty[N-1] + 1 + eat(N-1, (X - (1 + burger[N-1] + 1)))
    else:
        return patty[N]

print(eat(N, X))