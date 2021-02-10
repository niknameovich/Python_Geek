def my_dev(arg1,arg2):
    try :
         return arg1/arg2
    except ZeroDivisionError:
        print('Деление на ноль')

print(my_dev(15.89,9))