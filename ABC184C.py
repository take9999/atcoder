# ポイント：座標系を45度回転させて考えるとうまくいく　(x, y) -> (x-y, x+y)
# A. x1+y1 == x2+y2 -> x1' == x2'
# B. x1-y1 == x2-y2 -> y1' == y2'
# C. |x1-x2| + |y1-y2| <= 3 -> max(|x1' - x2'|, |y1' - y2'|) <= 3

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

# 移動なし
if x1 == x2 and y1 == y2:
    print(0)
# A,B,Cのいずれかの移動1回
elif x1+y1 == x2+y2 or x1-y1 == x2-y2 or abs(x1-x2)+abs(y1-y2) <= 3:
    print(1)
# A,B,Cのいずれかの移動2回
# AA -> 同じ向きの斜め移動2回は、1回と変わらないので除外
# AB -> 違う向きの斜め移動2回。(x1+x2)%2 == (y1+y2)%2 同じ格子状にいること。
# AC -> 座標系を45度変換して考えるとA,Cを満たすのは、 |y1' - y2'| <= 3
# BB -> 同じ向きの斜め移動2回は、1回と変わらないので除外
# BC -> ACと考え方同じ。座標系を45度変換して考えるとA,Cを満たすのは、 |x1' - x2'| <= 3
# CC -> |x1-x2| + |y1-y2| <= 6
elif (x1+x2) % 2 == (y1+y2) % 2 or abs((x1-y1)-(x2-y2)) <= 3 or abs((x1+y1)-(x2+y2)) <= 3 or abs(x1-x2)+abs(y1-y2) <= 6:
    print(2)
# A,B,Cのいずれかの移動3回
else:
    print(3)