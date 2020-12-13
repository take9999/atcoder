# 幅優先探索で各部屋の深さを見ていく
# ポイント「深さx+1の部屋には，深さxの部屋が少なくとも1つは繋がっている」
from collections import deque

# 部屋がn個、通路がm個
n, m = map(int, input().split())

# graphには、各部屋の隣接リストを入れる
graph = [[] for _ in range(n+1)]
for target_room_id in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 各部屋の深さを格納
dist = [-1] * (n+1)
dist[0] = 0
dist[1] = 0

# 最短距離で1番の部屋へ向かうための、一つ前の部屋の番号を入れる(複数存在する場合はひとつだけで良い)
pre = [-1] * (n+1)
pre[0] = 0
pre[1] = 0

# 「先頭から要素を取り出す」「末尾に要素を追加する」操作のみ行うためdequeを利用
d = deque()
d.append(1)

# 頂点jがdの要素(dに入っている)」ならば、それは「頂点jは既に訪問済」であることを表す
while d:
    now_room_id = d.popleft()
    for target_room_id in graph[now_room_id]:
        # target_roomは訪問済み：深さが確定済みなので何もしない
        if dist[target_room_id] != -1:
            continue
        # target_roomは未訪問：深さを確定させる(現在の部屋の深さプラス1)
        else:
            dist[target_room_id] = dist[now_room_id] + 1
            d.append(target_room_id)
            pre[target_room_id] = now_room_id

# 結果表示(2番目以降の部屋のみ表示)
ans = pre[2:]
if -1 not in ans:
    print("Yes")
    for a in ans:
        print(a)
else:
    print("No")
