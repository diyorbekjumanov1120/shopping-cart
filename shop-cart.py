with open('data.json') as file:
    lst = file.readlines()
    f_lst = list()

    for x in range(1, len(lst)-1):
        f_lst.append(lst[x].strip())
    
    s = list()
    for i in range(len(f_lst)):
        s += f_lst[i].split(':')
    
    s1 = ''
    for j in range(len(s)):
        if j % 2 == 1:
            if '$' not in s[j]:
                s1 += s[j]
            else:
                s1 += "'" + s[j][2:len(s[j])]
with open('data.txt', 'w') as w:
    w.write('[' + s1 + ']')

