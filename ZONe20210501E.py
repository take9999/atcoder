# 座標(1,1)から(R,C)へ向かう
# ある座標から次の座標へ移動できる条件とコストが与えられている。
# 頂点の数はRC
# 辺の数については、下向きの移動について、1<=i<rのためR通りとなるため、
# 計算量がR^2Cとなる。
#
# 頂点を2倍にして、通常の(r,c)と移動中の(r,c)の2種類を用意する。
# 通常の(r,c)から移動中の(r,c)へのコスト1の辺を張る
# 移動中の(r,c)から移動中の(r-1,c)へのコスト1の辺を張る
# 移動中の(r,c)から通常の(r,c)へコスト0の辺を張る
#

from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

R, C = map(int, input().split())
data = []
row = []
column = []

# 横方向への移動
for i in range(R):
    cost = list(map(int, input().split()))
    for j in range(C - 1):
        # 頂点fから頂点tへの移動コスト
        # 横への移動は、進むのも戻るのも同じコストcost[j]
        f = i * C + j
        t = i * C + j + 1
        row += [f, t]
        column += [t, f]
        data += [cost[j], cost[j]]

# 縦方向への移動（下方向への移動は、移動中の(r,c)にてコスト1で行う
for i in range(R - 1):
    cost = list(map(int, input().split()))
    for j in range(C):
        # 頂点fから頂点tへの移動コストはcost[j]
        # t':移動中の(r,c) から f':移動中の(r-1,c) へのコスト1の辺を張る
        f = i * C + j
        t = i * C + j + C
        row += [f, t + R * C]
        column += [t, f + R * C]
        data += [cost[j], 1]

# 通常の(r,c)と移動中の(r,c)間での移動
for i in range(R):
    for j in range(C):
        # 通常の(r,c)から移動中の(r,c)へのコスト1の辺を張る
        # 移動中の(r,c)から通常の(r,c)へコスト0の辺を張る
        f = i * C + j
        t = f + R * C
        row += [f, t]
        column += [t, f]
        data += [1, 0]

g = csr_matrix((data, (row, column)))
sp = shortest_path(g, indices=0)
print(int(sp[R * C - 1]))
