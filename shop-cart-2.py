import json
file = open('data-1.json')
data = file.read()

lst = list()
lst.append(data[:data.find('}') + 1])
lst.append(data[data.find('}') + 1:])
