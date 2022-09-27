N = int(input())
seq = list(map(int, input().split()))

odd, even = 0, 0

for i in range(N):
    if seq[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if (odd == even +1) or odd == even:
    print(1)
else:
    print(0)
