import math

percent = int(input('введите процент:'))
value = int(input('введите число:'))
print(value*percent/100)

# тест кириллицы в именах переменных
основание = float(input('введите число с точкой:'))
степень = int(input('введите степень числа'))
print(math.floor(основание ** степень),(основание ** степень))