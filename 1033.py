import sys
input = sys.stdin.readline

N = int(input())
ratio = [[] for _ in range(N)]
mass = [0] * (N)
visited = [False] * N

# 유클리드 호제법 함수
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

#비율에 맞춰 계산하기 위한 그래프 탐색
def DFS(v):
    visited[v] = True
    for i in ratio[v]:
        next = i[0]
        if not visited[next]:
            mass[next] = i[2] * mass[v] // i[1]
            DFS(next)

#관계리스트 생성
lcm = 1
for _ in range(N-1):
    a, b, p, q = map(int,input().split())
    ratio[a].append((b, p, q))
    ratio[b].append((a, q, p))
    lcm *= ((p * q) // gcd(p, q)) # 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것

mass[0] = lcm
DFS(0)

#최대 공약수 구하기
greatest_common_divisor = mass[0]
for i in range(1, N):
    greatest_common_divisor = gcd(greatest_common_divisor, mass[i])

#최대공약수로 각 질량을 나눠줌
for i in range(len(mass)):
    mass[i] = mass[i] // greatest_common_divisor
print(*mass)