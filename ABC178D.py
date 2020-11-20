s = 1000
mod = 10 ** 9 + 7

dp = [0]*(s+1)  # [0, 0, 0, ..., 0]
dp[0] = 1
for i in range(1, s+1):
    for j in range(0, (i-3)+1):
        dp[i] += dp[j]
        dp[i] %= mod

print(dp[s])
