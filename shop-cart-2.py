import json
file = open('data-1.json')
data = file.read()

lst = list()
lst.append(data[:data.find('}') + 1])
lst.append(data[data.find('}') + 1:])

total = 0

for half_data in lst:
    idx1 = half_data.find('$') + 1
    idx2 = half_data.find('"', idx1)
    itemPrice = float(half_data[idx1:idx2])

    idx1 = half_data.find('quantity') + 10
    idx2 = half_data.find('}', idx1)
    quantity = float(half_data[idx1:idx2])

    total += itemPrice * quantity

dic = {
    "shipping": 0,
    "total": total
}
file.close()

f = open('data-2.json', 'w')
j = json.dumps(dic, indent=4)
f.write(j)
