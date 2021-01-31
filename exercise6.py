startwith = float(input('отправной результат - '))
target = float(input('желаемый результат -'))
percent = float(input('введите интенсивность в процентах -'))
daystotarget = 0;
while startwith*(1+(percent/100)) < target:
    daystotarget+=1
    startwith = startwith*(1+(percent/100))
print(f'необходимо затратить {daystotarget+1} дней')
