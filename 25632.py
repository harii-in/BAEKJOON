import math

A, B = map(int, input().split())
C, D = map(int, input().split())

def minority(n, m):
    lst = list(range(n, m+1))

    if 1 in lst:
        lst.remove(1)
    
    for i in range(2, math.ceil(math.sqrt(m))):
        for tmp in lst:
            if tmp/i == 1:
                continue
            elif tmp%i == 0:
                lst.remove(tmp)
    return lst

yt = minority(A, B)
yj = minority(C, D)

if len(yt) > len(yj):
    print('yt')
elif len(yt) < len(yj):
    print('yj')
else:
    cnt = len(set(yt) & set(yj))
    if cnt % 2 == 0:
        print('yj')
    else: print('yt')