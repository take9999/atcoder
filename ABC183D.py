N, W = list(map(int, input().split()))
MAX_T = 200005
d = [0 for x in range(MAX_T)]

for i in range(N):
    s, t, p = list(map(int, input().split()))
    d[s] += p
    d[t] -= p

# 累積和の計算
for i in range(MAX_T-1):
    d[i+1] += d[i]

# チェック
for i in range(MAX_T):
    if d[i] > W:
        print("No")
        exit()
print("Yes")
