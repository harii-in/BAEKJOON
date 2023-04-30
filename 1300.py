import sys
input = sys.stdin.readline

N = int(input())
k = int(input())
ans = 0

# k번째 수는 k보다 클 수 없음
# A보다 작은 숫자가 몇개인지 찾아내면 
    # A가 몇 번째 숫자인지 알 수 있음.
start, end = 1, k

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, N+1):
        cnt += min(mid//i, N)
    
    if cnt >= k:
        ans = mid
        end = mid-1
    else:
        start = mid + 1

print(ans)