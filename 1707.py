import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# 테스트 케이스의 개수
K = int(input())

# 현재 노드와 이웃한 노드 탐색
def DFS(v):
    global result

    for neighbor in graph[v]:

        # 이웃 노드에 색칠이 되어있지 않다면
        if visited[neighbor] == 0:

            # 현재 노드가 1로 색칠되어 있다면 이웃 노드는 -1로 색칠
            if visited[v] == 1:
                visited[neighbor] = -1
            # 현재 노드가 -1로 색칠되어 있다면 이웃 노드는 1로 색칠
            if visited[v] == -1:
                visited[neighbor] = 1

            DFS(neighbor)

        # 이웃 노드에 색칠이 되어있다면    
        else:
            # 현재 노드와 이웃 노드의 색이 같다면 이분 그래프가 아님
            if visited[neighbor] == visited[v]:
                result = False
                return

for _ in range(K):

    v, e = map(int, input().split())
    visited = [0] *(v+1)    # 색칠 여부

    graph = [[] for _ in range(v+1)]

    # 양방향 간선 정보 저장
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    # 이분 그래프 여부
    result = True

    # 모든 노드에 대해 DFS 실행함으로써 이분 그래프 여부 확인
    for i in range(1, v+1):

        # 현재 노드가 색칠되어 있지 않다면
        if visited[i] == 0:

            # 현재 노드를 1로 색칠
            visited[i] = 1

            # 이웃한 노드에 대해서 색칠
            DFS(i)
            
            # 현재 노드로부터 이웃한 노드까지 색칠이 끝났는데 이분 그래프가 아니라면
            if not result:
                break
        
    if not result:
        print("NO")
    else:
        print("YES")