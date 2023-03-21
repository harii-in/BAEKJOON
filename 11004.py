# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# def quickSort(start, end, K):
#     global A
#     if start < end:
#         pivot = partition(start, end)
#         if pivot == K:
#             return
#         elif pivot < K:
#             quickSort(start, pivot-1, K)
#         else:
#             quickSort(pivot+1, end, K)

# def swap(i, j):
#     global A
#     tmp = A[i]
#     A[i] = A[j]
#     A[j] = tmp

# def partition(start, end):
#     global A

#     if start + 1 == end:
#         if A[start] > A[end]:
#             swap(start, end)
#         return end
    
#     mid = (start+end) // 2
#     swap(start, mid)
#     pivot = A[start]
#     i = start + 1
#     j = end

#     while i<=j:
#         while pivot > A[i] and i<len(A)-1:
#             i += 1
#         while pivot < A[j] and j>0:
#             j -= 1
#         if i <= j:
#             swap(i, j)
#             i += 1
#             j -= 1
    
#     A[start] = A[j]
#     A[j] = pivot
#     return j

# quickSort(0, N-1, K-1)
# print(A[K-1])


# 내 방식
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
print(A[K-1])