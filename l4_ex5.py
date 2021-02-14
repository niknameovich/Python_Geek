from functools import reduce

print(reduce(lambda prev, next : prev*next, [item for item in range(100,1001) if item % 2 == 0]))
