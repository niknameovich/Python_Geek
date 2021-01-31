num = input('введите число -')
maxval = 0
i = 0
while i < num.__len__():
    if int(num[i]) > maxval:
        maxval = int(num[i])
    i +=1
print(f'Максимальное целое число - {maxval}')
