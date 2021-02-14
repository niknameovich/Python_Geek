from sys import argv

try:
    print(f'расчет ЗП по формуле (выработка*ставка) + премия ='
          f'{(float(argv[1]) if float(argv[1]) > 0 else None) * (float(argv[2]) if float(argv[2]) > 0 else None) + (float(argv[3]) if float(argv[3]) > 0 else None)}')
except:
    print('Используйте числовые значения')