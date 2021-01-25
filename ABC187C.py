N = int(input())
dict1 = {}
dict2 = {}
find_flag = False
n_list = []

for i in range(N):
    n_list.append(input())

for input_str in n_list:

    if input_str.startswith('!'):
        o_str = input_str[1:]
        if o_str not in dict1:
            dict1[o_str] = True
    else:
        o_str = input_str
        if o_str not in dict2:
            dict2[o_str] = True

    if o_str in dict1 and o_str in dict2:
        print(o_str)
        find_flag = True
        break

if not find_flag:
    print("satisfiable")
