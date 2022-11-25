N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def pooling(size, x, y):
    half = size // 2
    if size == 2:
        ans = [matrix[x][y], matrix[x+1][y], matrix[x][y+1], matrix[x+1][y+1]]
        ans.sort()
        return ans[-2]

    left_top = pooling(half, x, y)
    right_top = pooling(half, x+half, y)
    left_bottom = pooling(half, x, y+half)
    right_bottom = pooling(half, x+half, y+half)

    ans = [left_top, right_top, left_bottom, right_bottom]
    ans.sort()

    return ans[-2]

print(pooling(N, 0, 0))