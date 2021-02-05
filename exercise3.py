seasons_map = ['winter','spring','summer','autumn']
seasons_map_dict = {0:'winter',1:'spring',2:'summer',3:'autumn',4:'winter'}
num = -1
while True:
    num = int(input('Put month number (1,12): '))
    if num > 0 and num <= 12:
        break
#using list
print('list season is ', seasons_map[num//3] if num < 12 else seasons_map[0])
# using dictionary
print('dictionary season is ', seasons_map_dict[num//3])




