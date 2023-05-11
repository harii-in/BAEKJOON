import sys, math
input = sys.stdin.readline

# 에스토스테네스의 체
MAX = 1005000
prime = [True] * MAX
prime[1] = False
for i in range(2, int(math.sqrt(MAX))):
    if prime[i]:
        for j in range(i+i, MAX, i):
            prime[j] = False

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

N = int(input())
while True:
    if prime[N] and isPalindrome(N):
        print(N)
        break
    N += 1