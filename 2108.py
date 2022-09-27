import sys
from collections import Counter

N = int(input())

tmp = []
for i in range(N):
    tmp.append(int(sys.stdin.readline()))

print(round(sum(tmp)/N))

tmp.sort()
print(tmp[int((N-1)/2)])

mode = Counter(tmp).most_common()   # [tmp값][빈도수]로 tmp값이 작고 빈도수가 높은 순으로 투플형태로 출력

if len(mode) > 1: #입력값이 여러개일때
    if mode[0][1] == mode[1][1]:    #2개 이상의 최빈 값이 있을시
        print(mode[1][0])
    else:
        print(mode[0][0])
else:   #입력값이 하나 이므로 예외 처리
    print(tmp[0])

print(max(tmp) - min(tmp))
