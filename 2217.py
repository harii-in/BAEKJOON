N = int(input())
rope = []
result = []

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse = True)   # 내림차순

for num in range(N):
    result.append(rope[num] * (num+1))

print(max(result))