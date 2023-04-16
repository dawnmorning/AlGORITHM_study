import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
def bfs(start):
    q = deque([start])
    visited = [0] * (n+1)
    visited[start] = 1
    answer = [0] * (n+1)
    while q:
        v = q.popleft()
        for i in barn[v]:
            if not visited[i]:
                answer[i] = answer[v] + 1
                visited[i] = 1
                q.append(i)
    return answer


barn = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    barn[a].append(b)
    barn[b].append(a)
# print(barn)
result = bfs(1)

answer1 = result.index(max(result))
answer2 = result[answer1]
answer3 = result.count(max(result))

print(answer1,answer2,answer3)