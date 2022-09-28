import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site = {}

for _ in range(N):
    id, ps = input().split()
    site[id] = ps

for _ in range(M):
    print(site[input().rstrip()])