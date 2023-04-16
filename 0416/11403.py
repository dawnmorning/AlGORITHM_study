# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, 
# i에서 j로 가는 경로가 있는지 없는지 구하는 문제

# 플로이드-와샬 알고리즘을 이용한 풀이
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


# 너 무조건 1중 for문으로 할 수 있니?
# O N^2 무조건 컷인 느낌
for i in range(n): # 거쳐가는 노드
    for j in range(n): # 시작 노드
        for k in range(n): # 도착노드
            # j -> i가 존재하면, i -> k 존재하면 j -> k 이어주기
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
for g in graph:
    print(*g)

# BFS
# from collections import deque
 
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0]*n for _ in range(n)]

# def bfs(x):
#     queue = deque()
#     queue.append(x)
#     check = [0 for _ in range(n)]
 
#     while queue:
#         q = queue.popleft()
 
#         for i in range(n):
#             if check[i] == 0 and graph[q][i] == 1:
#                 queue.append(i)
#                 check[i] = 1
#                 visited[x][i] = 1
 
# for i in range(0, n):
#     bfs(i)
 
# for i in visited:
#     print(*i)