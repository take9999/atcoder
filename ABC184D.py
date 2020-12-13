a, b, c = map(int, input().split())
X = 100
dp = [[[0 for z in range(X+1)] for y in range(X+1)] for x in range(X+1)]

# a, b, cが全て100
for i in range(X-1, -1, -1):
    for j in range(X-1, -1, -1):
        for k in range(X-1, -1, -1):
            if i+j+k == 0:
                continue
            else:
                now = 0
                now += dp[i+1][j][k] * i
                now += dp[i][j+1][k] * j
                now += dp[i][j][k+1] * k
                dp[i][j][k] = now/(i+j+k) + 1
print(dp[a][b][c])
