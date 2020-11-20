import itertools


def calc_cost(route_list, t_dict):
    """
    :param route_list: 移動する街の順番がtupleで入っている　例：(2, 3, 4)
    :param t_dict: 各街から他の街への移動コストの一覧
    :return: 全ての街を移動した際のコスト
    """

    total_cost = 0
    departure = 1  # スタートは1番の街

    for destination in route_list:
        total_cost += t_dict[departure][destination - 1]
        departure = destination

    # ゴールは1番の街
    total_cost += t_dict[route_list[-1]][0]

    return total_cost


N, K = list(map(int, input().split()))
t_dict = {}
ans = 0

for i in range(1, N+1):
    t_dict[i] = list(map(int, input().split()))

two_to_N_list = [x for x in range(2, N+1)]
for v in itertools.permutations(two_to_N_list, N-1):
    cost = calc_cost(v, t_dict)
    if cost == K:
        ans += 1
print(ans)