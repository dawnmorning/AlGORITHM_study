import sys
from collections import deque

# 미세먼지 확산 함수
def spread_dust(r, c, arr):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    new_arr = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] != -1:
                        new_arr[nr][nc] += arr[i][j] // 5
                        cnt += 1
                new_arr[i][j] += arr[i][j] - (arr[i][j] // 5) * cnt
            elif arr[i][j] == -1:
                new_arr[i][j] = -1

    return new_arr

# 공기청정기 작동 함수
def clean_air(r, c, arr, purifiers):
    new_arr = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] != -1:
                new_arr[i][j] = arr[i][j]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for p in purifiers:
        d = 0
        nr, nc = p
        while True:
            nr, nc = nr + dr[d], nc + dc[d]
            if not (0 <= nr < r and 0 <= nc < c) or new_arr[nr][nc] == -1:
                nr, nc = nr - dr[d], nc - dc[d]
                d = (d + 1) % 4
                nr, nc = nr + dr[d], nc + dc[d]
                if new_arr[nr][nc] == -1:
                    break
            new_arr[p[0] + dr[d]][p[1] + dc[d]], new_arr[nr][nc] = new_arr[nr][nc], 0

    return new_arr

# 입력
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기
purifiers = [(i, 0) for i in range(r) if arr[i][0] == -1]

# t초 동안 미세먼지 확산 및 공기청정기 작동
for _ in range(t):
    arr = spread_dust(r, c, arr)
    arr = clean_air(r, c, arr, purifiers)

# 남은 미세먼지 양 계산
answer = sum(map(sum, arr)) + 2

print(answer)  # 결과 출력
