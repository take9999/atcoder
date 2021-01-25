# 2次元領域について、繋がっている島が何個あるかを数える
# stackでもqueueでもいいので、繋がっている島のリストを一時保存できる領域を利用
# dfs(深さ優先探索)を用いて、繋がっている島をチェック

while True:
    w, h = list(map(int, input().split()))
    if w == h == 0:
        break

    ans = 0
    area_list = [list(map(int, input().split())) for _ in range(h)]
    seen = [[False] * w for _ in range(h)]
    move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


    def dfs(start_h, start_w):
        stack = [[start_h, start_w]]  # stackに最初の島の座標を入れる
        seen[start_h][start_w] = True

        while stack:
            sh, sw = stack.pop()

            # 繋がっている島を探索し、stackへ入れる
            for dh, dw in move:
                nh, nw = sh + dh, sw + dw
                if not (0 <= nh <= h-1) or not (0 <= nw <= w-1) or seen[nh][nw] or area_list[nh][nw] == 0:
                    continue
                seen[nh][nw] = True
                stack.append([nh, nw])


    for i in range(h):
        for j in range(w):
            # 既にチェック済みの座標もしくは海の場合はスキップ
            if seen[i][j] or area_list[i][j] == 0:
                continue
            else:
                ans += 1  # i,jを含む島をカウント
                dfs(i, j)  # i,jと繋がっている島の座標を全てチェック済みにする(seenを更新する)

    print(ans)
