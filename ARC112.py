# LからRの範囲で、A-B=Cになるような組み合わせの数を求める問題
# A=B+Cとして考える
# Bの範囲をL-LからR-Lまで（Lを引いた範囲）にすることで、0からR-Lまでになる。
# Cの範囲も同じ
# Aの範囲は、BとCがそれぞれLを引いた範囲にしているので、2Lを引いた範囲になる。（ポイント）
# まとめると、Aの範囲はL-2LからR-2Lとなるが、マイナスの値は条件に当てはまらないので、0からR-2Lにする。
# 0,1,2,,,R-2Lとみていくと、等差数列の和として計算することができる。


def solve(start, end):
    # R-2L
    n = end - start*2

    if n < 0:
        return 0
    else:
        ans = (n+1)*(n+2)//2
        return ans


T = int(input())

for i in range(T):
    L, R = map(int, input().split())
    print(solve(L, R))
