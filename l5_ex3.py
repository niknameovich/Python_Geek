from functools import reduce

limit = 20000
empanalytic = dict()

with open('exercise3.txt', 'r', encoding='utf-8') as calcfile:
    for line in map(lambda x: x.split(), calcfile):
        empanalytic[line[0]] = float(line[-1])
print(f'low salary employes - {[name for name,sal in empanalytic.items() if sal < limit]}')
print(f'average salary = {reduce(lambda x,y: x+y,empanalytic.values())/len(empanalytic)}')
