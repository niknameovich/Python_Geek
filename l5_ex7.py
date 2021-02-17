import json
from statistics import mean

catalog = list()
result = list()

with open('exercise7.txt', 'r', encoding='utf-8') as source:
    catalog = source.readlines()

result = {item[0]: float(item[-2])-float(item[-1]) for item in map(lambda x: x.split(), catalog)}
result['average_prof'] = mean([val for val in result.values() if val > 0])

with open('exercise7_result.json','w',encoding='utf-8') as rj:
    json.dump(result, rj)
with open('exercise7_result.json','r',encoding='utf-8') as tj:
    print(json.load(tj))