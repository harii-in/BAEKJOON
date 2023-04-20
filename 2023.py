import sys
input = sys.stdin.readline

N = int(input())

def isPrime(num):
    for i in range(2, int(int(num)**0.5)+1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            tmp = num*10 + i
            if isPrime(tmp):
                DFS(tmp)

DFS(2)
DFS(3)
DFS(5)
DFS(7)