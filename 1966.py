T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[M] = 'target'
    cnt = 0

    while True:
        if imp[0] == max(imp):
            cnt += 1

            if idx[0] == 'target':
                print(cnt)
                break
            else:
                #imp.pop(0)
                #idx.pop(0)
                del imp[0]
                del idx[0]
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))