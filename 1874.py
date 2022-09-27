n = int(input())

tmp = 1
flag = 0
stack = []
ans = []
for _ in range(n):
    num = int(input())

    while tmp <= num:
        stack.append(tmp)
        ans.append("+")
        tmp += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)