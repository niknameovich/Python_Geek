import math

def parselessons(contextfile, target=dict()):
    with open(contextfile, 'r', encoding='utf-8') as context:
        lessons = context.readlines()
    for expprogram in map(lambda x: x.split(':'), lessons):
        target[expprogram[0]] = math.fsum([int(x[:x.index('(')]) for x in expprogram[-1].split() if x != '-'])
    return target


print(parselessons('exercise6.txt'))
