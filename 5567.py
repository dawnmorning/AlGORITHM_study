import sys
input = sys.stdin.readline
from collections import deque
def bfs(start):
    q = deque([start])
    cnt = 0
    visited[start] = 1
    while q:
        value = q.popleft()
        cnt += 1
        for j in arr[value]:
            if not visited:
                visited[j] = visited[value] + 1
                q.append(j)
n = int(input())
m = int(input())
arr = [[] for i in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int , input.split())
    arr[u].append(v)
    arr[v].append(u)
bfs(1)



