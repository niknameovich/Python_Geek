# using lambda
print(list(filter(lambda x: x%20==0 or x%21==0, range(20,240))))

#using generator
print([x for x in range(20,240) if x%20==0 or x%21==0])