def my_func(x,y):
    try:
        float_x = float(x)
        int_y = int(y)
        for pow in range(int_y):
            float_x+=float_x
        return 1/float_x
    except ValueError:
        print('incorrect argument values')

print(my_func(input('put any real number here-'),input('put negative integer-')))