atributes = ['name','price','count','UOM']
products = []
analytic = {}
while True:
    if int(input('Добавить товар ?')) <= 0:
        break
    else:
        products.append((len(products) + 1,dict.fromkeys(atributes)))
        for key in atributes:
            products[-1][-1][key] = input(f'Введите значение {key}:')
for product in products:
    for key in atributes:
        if not analytic.keys().__contains__(key):
            analytic[key] = []
        analytic[key].append(product[-1][key])
print(analytic)



