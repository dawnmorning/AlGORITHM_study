n = int(input())
scehdule = [list(map(int, input().split()))for _ in range(n)]
dp = [0 for _ in range(n+1)]


# 1. 상담에 필요한 일 수가 퇴사일을 넘어가는 경우
# -> 해당 일자에 일을 할 수 없으니 다음날의 dp 값을 그대로 가져온다. (dp의 최댓값인 dp[i+1])

# 2. 퇴사일을 넘어가지 않을 경우
# (i) 오늘 상담을 하지 않을 경우 : dp[i+1] (지난 상담까지의 보수)
# (ii) 오늘 상담을 할 경우 : (dp[오늘 날짜 + 오늘 시작할 상담에 필요한 일 수] + (상담 보수))

for i in range(n-1,-1,-1):
    if i + scehdule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], scehdule[i][1] + dp[i+scehdule[i][0]])

print(dp[0])