# ヒストグラム内の最大長方形の面積を求める問題
#
# stackには、長方形情報 rect (長方形の高さ height, 左端位置 pos)を持たせる。
# ヒストグラムを左から右へ進めながら、以下の処理を行う。
#
# 1.stackが空の場合：stackに 現在位置の rect を追加
#
# 2.stackの頂点にある長方形の高さが、現在位置の高さより低い場合：stackに 現在位置の rect を追加
#
# 3.stackの頂点にある長方形の高さが、現在位置の高さと等しい場合：何もしない
#
# 4.stackの頂点にある長方形の高さが、現在位置の高さより高い場合：
# 　stackが空でなく、stackの頂点にある長方形の高さが rect の高さ以上である限り、stackから長方形を取り出し、面積を計算し最大値を更新する。
# 　(各長方形の横の長さは、現在の位置 i と長方形情報の左端位置 posから計算できる。)
# 　stackに rect を追加する。ただし、rect の左端位置 pos は最後にstackから取り出した長方形の pos の値とする。
#

N = int(input())
hist_list = map(int, input().split())
stack = []
max_size = 0

for pos, height in enumerate(hist_list):
    rect = [height, pos]

    # stackが空の場合
    if len(stack) == 0:
        stack.append(rect)

    # stackが空ではない場合
    else:
        last_rect_of_stack = stack[-1]
        last_rect_height = last_rect_of_stack[0]
        last_rect_pos = last_rect_of_stack[1]

        # stackの頂点にある長方形の高さが、現在位置の高さより低い場合
        if last_rect_height < height:
            stack.append(rect)

        # stackの頂点にある長方形の高さが、現在位置の高さと等しい場合
        elif last_rect_height == height:
            pass

        # stackの頂点にある長方形の高さが、現在位置の高さより高い場合
        else:
            last_popped_pos = None

            while stack:
                last_rect_of_stack = stack[-1]
                last_rect_height = last_rect_of_stack[0]
                last_rect_pos = last_rect_of_stack[1]

                # stackの頂点にある長方形の高さが、現在位置の高さより高い場合はpopして面積計算し、最大値比較を行う。
                if height <= last_rect_height:
                    stack.pop()
                    last_popped_pos = last_rect_pos

                    # ひとつ前の rect のサイズを計算して、最大値を更新
                    last_rect_width = pos - last_popped_pos
                    last_rect_size = last_rect_width * last_rect_height
                    if max_size < last_rect_size:
                        max_size = last_rect_size

                    # stackが空になった場合、
                    # 現在位置の高さ　と　最後にpopした位置（現在位置の高さ以上の位置）を rect としてstackへ入れる。
                    # 現在位置での探索は終了する。（break)
                    if len(stack) == 0:
                        rect = [height, last_popped_pos]
                        stack.append(rect)
                        break
                # popした長方形の高さが、現在位置の高さより小さくなった場合、
                # 現在位置の高さ　と　最後にpopした位置（現在位置の高さ以上の位置）を rect としてstackへ入れる。
                # 現在位置での探索は終了する。（break)
                else:
                    rect = [height, last_popped_pos]
                    stack.append(rect)
                    break

print(max_size)
