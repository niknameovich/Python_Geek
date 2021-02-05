int_var = 1
str_var = 'vatrushka'
float_var = 15.1
array_var = [10,15]
byte_var = bytes(1)
mylist = [int_var,byte_var,str_var,float_var,array_var]

for item in mylist:
    print(type(item), "это целое число !" if type(item) == type(int_var) else "это что то другое")