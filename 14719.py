H, W = map(int, input().split())
block = list(map(int, input().split()))

total = 0

for i in range(1, W-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    lowest = min(left_max, right_max)

    if block[i] < lowest:
        total += lowest - block[i]

print(total)