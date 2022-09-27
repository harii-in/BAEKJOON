num = int(input())

zero = []
for i in range(num):
    s = int(input())
    if s == 0:
        del zero[-1]
    else:
        zero.append(s)
    
print(sum(zero))