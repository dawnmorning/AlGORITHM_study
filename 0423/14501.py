n = int(input())
scehdule = [list(map(int, input().split()))for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    if i + scehdule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], scehdule[i][1] + dp[i+scehdule[i][0]])
        
print(dp[0])