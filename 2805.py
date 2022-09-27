N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    h = 0

    for i in tree:
        if i >= mid:
            h += i - mid
    
    if h >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)