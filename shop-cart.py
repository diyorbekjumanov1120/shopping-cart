with open('data.json') as file:
    f_str = file.read()
    i1 = f_str.find('{')
    f_str = f_str[i1+1:]
    i2 = f_str.find('}')
    f_str = f_str[:i2].split(",")
    w = open('data.txt', 'w')
    w.write("['")
    lst = list()
    for x in f_str:
        if x != "":
            lst_1 = (x.strip().split(':'))[1]
            if '"' in lst_1 and '$' not in lst_1:
                w.write(lst_1[1:-1] + "',")
            elif '$' in lst_1:
                w.write(lst_1[2:-1] + ",")
            else:
                w.write(lst_1 + "]")