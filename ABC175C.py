x, k, d = 10, 1, 2  # 現在地点、残り移動回数、1回の移動距離

now_point = abs(x)
remain_move = k

# ゼロに近い地点までの移動回数を算出
to_zero_kaisu = min(now_point // d, remain_move)

now_point -= d * to_zero_kaisu
remain_move -= to_zero_kaisu

if remain_move % 2 == 1:
    now_point = now_point - d

ans = abs(now_point)
print(ans)
