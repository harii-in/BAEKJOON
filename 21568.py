A, B, C = map(int, input().split())

# 최대공약수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# 유클리드 호제법 함수
def Execute(a, b):
    ret = [0]*2
    # 처음 시작하는 x, y는 이전 x와 이전 y가 없으므로 각각 1, 0으로 지정
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a//b
    v = Execute(b, a%b) # 재귀 형태로 유클리드 호제법 수행
    # 역순으로 올라오면서 x, y를 계산하는 로직
    ret[0] = v[1]
    ret[1] = v[0] - v[1]*q
    return ret
# 재귀 방식으로 알아낸 최종 x, y는 ax + by = gcd(a, b)를 만족

# C/gcd(A, B) = K라 가정 시 최초 방정식의 해는 Kx, Ky로 구할 수 있음
mgcd = gcd(A, B)

if C % mgcd != 0:
    print(-1)
else:
    mok = int(C / mgcd)     # K
    ret = Execute(A, B)
    # print(ret[0] * mok, end=' ')
    # print(ret[1] * mok)
    print(ret[0] * mok, ret[1] * mok)