import sys
input = sys.stdin.readline

N = int(input())

Score = []
for _ in range(3):
    Score.append(list(map(int, input().split())))

total_Score = [0]*N

for i in range(len(Score)):
    rank = []

    for j in range(N):
        tmp = 1 
        total_Score[j] += Score[i][j]

        for k in range(N):
            if Score[i][j] < Score[i][k]:
                tmp += 1
        rank.append(tmp)
    print(*rank)

total_rank = []
for i in range(N):
    tmp = 1
    
    for j in range(N):
        if total_Score[i] < total_Score[j]:
            tmp += 1
    total_rank.append(tmp)
print(*total_rank)