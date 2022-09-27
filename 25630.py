N = int(input())
st = list(input())

cnt = 0
for i in range(N//2):
    if st[i] == st[-(i+1)]:
        continue
    else:
        st[-i] = st[i]
        cnt += 1

print(cnt)