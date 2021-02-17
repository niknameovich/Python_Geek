import functools

def fact (n):
    i = 1
    while i <= n:
        yield functools.reduce(lambda x,y:x*y,range(1,i+1))
        i+=1

for el in fact(50):
    print(f'{el=}')
