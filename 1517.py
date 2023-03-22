import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
cnt = 0

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return 0
        mid = (low + high) // 2
        cnt = sort(low, mid) + sort(mid, high)
        cnt += merge(low, mid, high)
        return cnt

    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        cnt = 0

        while l < mid and h < high:
            if arr[l] <= arr[h]: # 같은 숫자인 경우도 포함
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
                cnt += mid - l

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

        return cnt

    return sort(0, len(arr))


cnt = merge_sort(A)
print(cnt)