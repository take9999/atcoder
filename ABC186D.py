N = int(input())
A = map(int, input().split())

# sortすると1<= i < j <= Nの順に並ぶ（O(NlogN))
# 1, 2, 5, 14
# j=0 A[j]=1  -> なし
# j=1 A[j]=2  -> (2,1)
# j=2 A[j]=5  -> (5,1), (5,2) これは、5*2 - (1+2)
# j=3 A[j]=14 -> (14,1),(14,2),(14,5) これは、14*3 - (1+2+5)
# 式を汎用化すると、A[j] * j - j未満までの累積和　と表せる

A = sorted(A)
ruisekiwa = 0
ans = 0
for j in range(0, N):
    ans += A[j] * j
    ans -= ruisekiwa
    ruisekiwa += A[j]

print(ans)