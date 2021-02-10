sumfromstr = 0

def my_func(listvalues: str):
    result = 0
    for item in listvalues.split():
        if item == 'q':
            break
        else:
            result += float(item)
    return result

while (True):
    currentstr = input('put any numbers split " "-')
    sumfromstr+=my_func(currentstr)
    print(f'your total score is {sumfromstr}')
    if currentstr.__contains__('q'):
        break