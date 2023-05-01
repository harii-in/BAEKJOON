import sys
input = sys.stdin.readline
import heapq

N = int(input())
card = []

for _ in range(N):
    heapq.heappush(card, int(input()))
card.sort()

if len(card) == 1:
    print(0)
else:
    ans = 0
    while len(card) > 1:
        data1 = heapq.heappop(card)
        data2 = heapq.heappop(card)
        ans += (data1 + data2)
        heapq.heappush(card, data1 + data2)
    print(ans)