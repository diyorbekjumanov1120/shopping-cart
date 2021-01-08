import json


def itemPrice(half_data):
    idx1 = half_data.find('$') + 1
    idx2 = half_data.find('"', idx1)
    return float(half_data[idx1:idx2])


def quantity(half_data):
    idx1 = half_data.find('quantity') + 11
    idx2 = half_data.find('}', idx1)
    return float(half_data[idx1:idx2])


file = open('data-1.json')
data = file.read()

lst = list()
lst.append(data[:data.find('}') + 1])
lst.append(data[data.find('}') + 1:])

total = 0

for half_data in lst:
    total += itemPrice(half_data) * quantity(half_data)

dic = {
    "shipping": 0,
    "total": total
}
file.close()

f = open('data-2.json', 'w')
j = json.dumps(dic, indent=4)
f.write(j)
