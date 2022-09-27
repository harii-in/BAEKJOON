T = int(input())

for _ in range(T):
    cnt = 0
    stack = list(input())

    for x in stack:
        if x == '(':
            cnt += 1
        elif x == ')':
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
