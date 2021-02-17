from itertools import count,cycle
from sys import argv

intargs = list(map(int,argv[1:]))

def pseudocounter(iterargs):
    if iterargs[0]==1:
        for item in count(iterargs[1]):
            if item <=iterargs[2]:
                print(item)
            else:
                break
    else:
        pass

def pseudorandom(iterargs):
    if iterargs[0] == 2:
        source = [5, 0.125, 86, 75, 1 ,0]
        for num,item in cycle(enumerate(source)):
            if num <= iterargs[2]:
                print(item)
            else:
                break
    else:
        pass

pseudocounter(intargs)
pseudorandom(intargs)