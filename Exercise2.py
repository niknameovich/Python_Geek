seconds = int(input('Введите количество секунд: '))
myformat = f'часы = {seconds // 3600};минуты = {(seconds % 3600)//60};секунды = {(seconds % 3600) % 60};'
print(myformat)
