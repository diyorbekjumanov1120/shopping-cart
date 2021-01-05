with open('data.json') as file:
    lst = file.readlines()
    f_lst = list()

    for x in range(1, len(lst)-1):
        # f_lst.append(lst[x].strip().split(':'))
        # print(lst[x].strip().split(':'))
        d = lst[x].strip().split(':')
        value = d[1][1:len(d[1])-2]
        # for y in range(len(d)):
        if len(d[1]) > 1:
            if '$' not in value:
                f_lst.append(value)
            else:
                f_lst.append(value[1:])
        else:
            f_lst.append(d[1])
    
    value_str = open('data.txt', 'w')
    value_str.write("['")
    for x in range(len(f_lst) - 1):
        value_str.write(f_lst[x] + "','")
    value_str.write(f_lst[len(f_lst) - 1] + "']")
    value_str.close()

