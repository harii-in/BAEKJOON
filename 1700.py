N, K = map(int, input().split())
product = list(map(int, input().split()))
multi = [0] * N
use = swap = max_idx = 0

for x in product[:]:
    # multi안에 현재 넣으려는 같과 같은게 있으면 넘어가기
    if x in multi:
        product.remove(x)
        continue 
    # multi가 비어있으면 넣어주기
    elif 0 in multi: 
        multi[multi.index(0)] = x
        product.remove(x)
    # multi 자리 찾기
    else:
        for i in multi:
            # 멀티탭에 있는 제품 중 이후 사용하는 제품이 없는 경우
            if i not in product:
                swap = i
                break
            
            # 멀티탭에 있는 제품 중 가장 나중에 사용하는 제품 교체.
            elif max_idx < product.index(i):
                max_idx = product.index(i)
                swap = i
        
        multi[multi.index(swap)] = x
        product.remove(x)
        max_idx = 0
        use += 1

print(use)