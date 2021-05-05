# dequeを利用して計算量を減らす

from collections import deque


s = deque()
rev = False

for i in input():
    if i == 'R':
        rev = not rev
    # 反転中の場合は、dequeの先頭に入れる
    elif rev:
        # 先頭に入れる際に、同じ文字が連続している場合は、新しい文字を追加せずに削除する。
        if s and s[0] == i:
            s.popleft()
        else:
            s.appendleft(i)
    # 反転中ではない場合は、dequeの末尾に入れる
    else:
        # 末尾に入れる際に、同じ文字が連続している場合は、新しい文字を追加せずに削除する。
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
if rev:
    s = reversed(s)
print("".join(s))
