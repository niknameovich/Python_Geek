def int_func(customstr:str):
    return customstr.title()
def int_func_custom(customstr:str):
    result = ''
    customarray = customstr.split()
    for word in customarray:
        result += f'{word.capitalize()} '
    return result

while True:
    ntext = input('put your text here - ')
    if ntext == 'q':
        break
    else:
        print(f'func with title result - {int_func(ntext)}')
        print(f'funct with array and capitalize result - {int_func_custom(ntext)}')

