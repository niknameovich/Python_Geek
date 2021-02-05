custom_str = input('put your phrase here - ')
custom_list = custom_str.split(' ')
for item in custom_list:
    print(f'элемент {custom_list.index(item)+1} равен {item[:10]}')
