N = int(input())
t_list = []
total_t = 0
total_a = 0
city = 0

for n in range(N):
    a, b = map(int, input().split())
    t_list.append([a+b, a])
    total_a += a

sorted_t_list = sorted(t_list, key=lambda x: x[0], reverse=True)

for i, one_city in enumerate(sorted_t_list):
    total_t += one_city[0]
    total_a -= one_city[1]
    city += 1
    if total_a < total_t:
        print(city)
        break
