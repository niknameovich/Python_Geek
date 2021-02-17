with open('mytestfile.txt','w') as myfile:
    while True:
        cstr = input('введите строку данных -')
        if cstr == '':
            break
        else:
            myfile.write(f'{cstr} \n')
