# A-Eの項目全てがx以上であるかどうかを判定することを考えると、
# 各項目の値を0、1の2パターンで表現出来れば良いため、
# せいぜい2^5=32種類の組み合わせのみ確認すれば良いことになる。

n = int(input())
m = 5

members = []
for i in range(n):
    members.append(list(map(int, input().split())))

# xの値について、二分探索を行う
ac = 0
wa = 1001001001
while ac+1 < wa:
    wj = (ac+wa)//2
    s = set()
    # print(wj)

    for i in range(n):
        x = 0
        for j in range(m):
            if members[i][j] >= wj:
                # 二進数の論理和
                # print(j, bin(1<<j))
                x |= 1 << j
        s.add(x)

    s_list = list(s)
    ok = False
    for i in range(len(s_list)):
        for j in range(i+1):
            for k in range(j+1):
                pass
                # print(k, j, i)
                if (s_list[i]|s_list[j]|s_list[k]) == (1 << m)-1:
                    ok = True
    if ok:
        ac = wj
    else:
        wa = wj
    # print(ac, wa, wj, s)
print(ac)

