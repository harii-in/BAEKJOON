import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = list(input().rstrip())
A, C, G, T = map(int, input().split())
result = 0

tmp = {"A":0, "C":0, "G":0, "T":0}
for i in DNA[:P]:
    tmp[i] += 1

if tmp ["A"] >= A and tmp ["C"] >= C and tmp ["G"] >= G and tmp ["T"] >= T:
    result += 1

for k in range(len(DNA)-P):
    tmp[DNA[k]] -= 1
    tmp[DNA[k+P]] += 1
    if tmp ["A"] >= A and tmp ["C"] >= C and tmp ["G"] >= G and tmp ["T"] >= T:
        result += 1

print(result)


# 두 번째 시도 - 책
# S, P = map(int, input().split())
# DNA = list(input())
# goal = list(map(int, input().split()))

# tmp = [0]*4
# check = 0
# result = 0

# def add(x):
#     global check, tmp, goal
#     if x == 'A':
#         tmp[0] += 1
#         if tmp[0] == goal[0]:
#             check += 1
#     elif x == 'C':
#         tmp[1] += 1
#         if tmp[1] == goal[1]:
#             check += 1
#     elif x == 'G':
#         tmp[2] += 1
#         if tmp[2] == goal[2]:
#             check += 1
#     elif x == 'T':
#         tmp[3] += 1
#         if tmp[3] == goal[3]:
#             check += 1

# def remove(x):
#     global check, tmp, goal
#     if x == 'A':
#         if tmp[0] == goal[0]:
#             check -= 1
#         tmp[0] -= 1
#     elif x == 'C':
#         if tmp[1] == goal[1]:
#             check -= 1
#         tmp[1] -= 1
#     elif x == 'G':
#         if tmp[2] == goal[2]:
#             check -= 1
#         tmp[2] -= 1
#     elif x == 'T':
#         if tmp[3] == goal[3]:
#             check -= 1

# for i in range(4):
#     if goal[i] == 0:
#         check += 1

# for i in range(P):
#     add(DNA[i])
# if check == 4:
#     result += 1

# for i in range(P, S):
#     j = i-P
#     add(DNA[i])
#     remove(DNA[j])
#     if check == 4:
#         result += 1

# print(result) 

# 시긴초과
# A, C, G, T = map(int, input().split())
# for i in range(0, S-P+1):
#     a_cnt, c_cnt, g_cnt, t_cnt = 0, 0, 0, 0
#     tmp = DNA[0+i:P+i]
    
#     a_cnt = tmp.count("A")
#     c_cnt = tmp.count("C")
#     g_cnt = tmp.count("G")
#     t_cnt = tmp.count("T")

#     if a_cnt == A and c_cnt == C and g_cnt == G and t_cnt == T:
#         result += 1
# print(result)