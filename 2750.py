N = int(input())

num = []
for _ in range(N):
    num.append(int(input()))

# 일반 정렬
num = sorted(num)

# 버블정렬
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):     #(시작, 마지막, 간격)
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(num)

# 삽입 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

insertion_sort(num)

# 출력
for i in num:
    print(i)