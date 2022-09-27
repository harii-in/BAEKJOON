N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

def binary(target, N, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == N[mid]:
        return 1
    elif target < N[mid]:
        return binary(target, N, start, mid-1)
    else:
        return binary(target, N, mid + 1, end)
    

for i in M_list:
    start = 0
    end = N -1
    print(binary(i, N_list, start, end))
