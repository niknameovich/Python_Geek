mylist = [50, 50, 15,14,14,10,10,10,5,3,3]
num = 0
while True:
    num = int(input('put your lucky num here:'))
    if num <= 0:
        print('lets go back to nature')
        break
    else:
        try:
            mylist.insert(len(mylist) - mylist[::-1].index(num), num)
        except ValueError:
            if mylist[0] < num:
                mylist.insert(0,num)
            elif mylist[-1] > num:
                mylist.append(num)
            else:
                for item in mylist:
                    if item < num:
                        mylist.insert(mylist.index(item), num)
                        break
print(mylist)