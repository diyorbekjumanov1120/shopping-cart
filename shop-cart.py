with open('data.json') as file:
    f_str = file.read()
    i1 = f_str.find('{')
    f_str = f_str[i1+1:]
    i2 = f_str.find('}')
    f_str = f_str[:i2].split(",")
    w = open('data.txt', 'w')
    w.write("['")
    lst = list()
    # lst_1 = list()
    for x in f_str:
        if x != "":
            lst_1 = (x.strip().split(':'))[1]
            if '"' in lst_1 and '$' not in lst_1:
                w.write(lst_1[1:-1] + "',")
            elif '$' in lst_1:
                w.write(lst_1[2:-1] + ",")
            else:
                w.write(lst_1 + "]")
    # print(lst_1)
    # lst.append(lst_1[0][1][1:-1])
    # lst.append(lst_1[1][1][2:-1])
    # lst.append(lst_1[2][1])

    # print(lst)




    # lst = file.readlines()  # We move the json file to the list view
    # f_lst = list()  # the values ​​in this list are aggregated

    # for x in range(1, len(lst)-1):
    #     d = lst[x].strip().split(':')
    #     value = d[1][1:len(d[1])-2]
    #     if len(d[1]) > 1:
    #         if '$' not in value:
    #             f_lst.append(value)
    #         else:
    #             f_lst.append(value[1:])
    #     else:
    #         f_lst.append(d[1])
    
    # value_str = open('data.txt', 'w')
    # value_str.write("['")
    # for x in range(len(f_lst) - 1):
    #     value_str.write(f_lst[x] + "','")
    # value_str.write(f_lst[len(f_lst) - 1] + "']")
    # value_str.close()

