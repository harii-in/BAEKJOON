from collections import deque

queue = deque()
ans = []

N, K = map(int, input().split())

for i in range(1, N+1):
    queue.append(i)

while queue:
    for j in range(K-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print("<", end="")
for x in range(len(ans)-1):
    print(ans[x], end=", ")
print(ans[-1], end="")
print(">")