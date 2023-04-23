n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
minV = int(1e9)
maxV = -int(1e9)

# 처음부터 시작하도록 하지.
answer = number[0]

def dfs(idx):
    global answer
    global minV, maxV

    if idx == n:
        if answer > maxV:
            maxV = answer
        if answer < minV:
            minV = answer
        return

    for i in range(4):
        tmp = answer
        if operator[i] > 0:
            if i == 0:
                answer += number[idx]
            elif i == 1:
                answer -= number[idx]
            elif i == 2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else:
                    answer = (-answer // number[idx]) * -1

            # 첫 번째 숫자에 첫 연산자를 넣고 DFS를 돌린다음

            # 다시 백트래킹을 통해 원래 상태로 돌린 후

            # 두 번째 연산자를 넣고 DFS를 돌린다음 다시 백트래킹으로 원래 상태로 돌려

            # 모든 경우의 수를 찾아내야 한다.
            operator[i] -= 1
            dfs(idx+1)
            answer = tmp
            operator[i] += 1


dfs(1)
print(maxV)
print(minV)