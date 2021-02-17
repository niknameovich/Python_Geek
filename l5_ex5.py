from functools import reduce

startnum = 5
endnum = 50
step = 1

with open('exercise5.txt', 'w') as source:
    for nums in range(startnum, endnum, step):
        source.write(f'{nums} ')

with open('exercise5.txt', 'r') as target:
    print(f'sum = {reduce(lambda x,y:x+y, map(int,target.read().split()))}')
