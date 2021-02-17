with open('venv\exercise2','r') as calcfile_stat:
    flines = calcfile_stat.readlines()
    print(f'количество строк в файле = {len(flines)}')
    for row,line in enumerate(flines,1):
        print(f'количество слов в строке {row} = {len(line.split())}')
