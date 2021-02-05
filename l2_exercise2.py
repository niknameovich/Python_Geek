mylist = []
while True:
    nextelement = input('Put your element here: ')
    if nextelement != 'break':
        mylist.append(nextelement)
    else:
        break
for item in mylist[::2]:
    mylist.insert(mylist.index(item)+1, mylist.pop(mylist.index(item)))
print(mylist)